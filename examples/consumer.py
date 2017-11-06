from confluent_kafka import Consumer, KafkaError


def create_consumer():
    return Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'example.group',
        'default.topic.config': {
            'auto.offset.reset': 'smallest'
        }
    })


def consume_topic(topic, callback):
    consumer = create_consumer()
    consumer.subscribe([topic])

    while True:
        message = consumer.poll()

        if not message.error():
            callback(message.value())

        elif message.error().code() != KafkaError._PARTITION_EOF:
            print(message.error())
            break

    consumer.close()
