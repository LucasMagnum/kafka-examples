Kafka Examples
==============

Simple Kafka consumers and producers examples.


# Examples

    - [x] Produce a raw string and consume it
    - [x] Produce a dict/list and consume it
    - [ ] Produce a message following a schema and consume it


# How to run

    # Start Kafka
    $ docker-compose start

    # Raw string examples
    $ python examples/produce_raw_string.py
    $ python examples/consume_raw_string.py

    # Dict & list examples
    $ python examples/produce_data_structure.py
    $ python examples/consume_data_structure.py

    # Message following schema
    $ python examples/produce_schema.py
    $ python examples/consume_schema.py
