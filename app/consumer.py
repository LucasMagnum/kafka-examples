from confluent_kafka import Consumer, KafkaError


def create_consumer():
    return Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'example.group',
        'default.topic.config': {
            'auto.offset.reset': 'smallest'
        }
    })


if __name__ == '__main__':
    topic = 'example-topic'

    consumer = create_consumer()
    consumer.subscribe([topic])

    while True:
        message = consumer.poll()

        if not message.error():
            print("Received message: %s" % message.value().decode('utf-8'), type(message.value()))

        elif message.error().code() != KafkaError._PARTITION_EOF:
            print(message.error())
            break

    consumer.close()
