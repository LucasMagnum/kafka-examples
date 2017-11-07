import json

from producer import produce_message


if __name__ == '__main__':
    data = json.dumps({
        'message': 'Hello Kafka!',
        'tags': ['message', 'hello_world']
    })
    produce_message('example-topic', data)
