import os
from kafka import KafkaClient
from config import config

flask_config = os.getenv('FLASK_CONFIG') or 'default'
kafka_uri = config[flask_config].KAFKA_URI


class Pkafka:
    def __init__(self):
        self.bootstrap_servers = kafka_uri

    def check_version(self):
        version = KafkaClient(bootstrap_servers=self.bootstrap_servers).check_version()
        return version
