import json

from consumer import consume_topic


def consume_callback(message):
    json_message = json.loads(message)
    print("Received message: %s - %s" % (json_message, type(json_message)))


if __name__ == '__main__':
    consume_topic('example-topic', consume_callback)
