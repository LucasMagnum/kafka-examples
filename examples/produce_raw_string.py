from producer import create_producer


if __name__ == '__main__':
    producer = create_producer()

    data = 'Hello Kafka!'
    producer.produce('example-topic', data.encode('utf-8'))
    producer.flush()

    print("Message produced")
