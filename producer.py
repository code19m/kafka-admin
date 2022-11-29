from random import choice
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
from kafka import KafkaProducer
import json

if __name__ == '__main__':

    producer = KafkaProducer(bootstrap_servers="192.168.254.139:9092")
    data = json.dumps(
        {
            "action": "ADD_USER",
            "user": {
                "id": 10,
                "full_name": "Nuriddin Obidjonov Olimjon o'g'li",
                "pinfl": "123412341234",
                "mob_phone_no": "",
                "email": "",
                "home_phone": "",
                "image": "",
                "current_organ_tin": "",
            },
        }
    ).encode("utf-8")
    producer.send("HR_USERS_TEST", data)
    print("Event sent!!!")
