from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from kafka import KafkaProducer


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    parser.add_argument('topic_name')    
    parser.add_argument('message')
    args = parser.parse_args()

    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])

    producer = KafkaProducer(bootstrap_servers=config.get("bootstrap.servers"))

    producer.send(
        topic=args.topic_name,
        value=str(args.message).encode("utf-8")
    )

    producer.flush()
