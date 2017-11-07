import json

from producer import create_producer


if __name__ == '__main__':
    producer = create_producer()

    data = json.dumps({
        'message': 'Hello Kafka!',
        'tags': ['message', 'hello_world']
    })
    producer.produce('example-topic', data)
    producer.flush()

    print("Message produced")
