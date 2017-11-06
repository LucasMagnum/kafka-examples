from confluent_kafka import Producer


def create_producer():
    return Producer({
        'bootstrap.servers': 'localhost:9092'
    })
