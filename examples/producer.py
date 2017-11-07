from confluent_kafka import Producer


def produce_message(topic, message):
    producer = create_producer()
    producer.produce(topic, message)
    producer.flush()
    print("Message produced")


def create_producer():
    return Producer({
        'bootstrap.servers': 'localhost:9092'
    })
