from consumer import consume_topic


def consume_callback(message):
    print("Received message: %s" % message.decode('utf-8'))


if __name__ == '__main__':
    consume_topic('example-topic', consume_callback)
