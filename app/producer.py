from confluent_kafka import Producer


def create_producer():
    return Producer({
        'bootstrap.servers': 'localhost:9092'
    })


if __name__ == '__main__':
    topic = 'example-topic'

    producer = create_producer()

    data = 'Hello Kafka!'
    producer.produce(topic, data.encode('utf-8'))
    producer.flush()
