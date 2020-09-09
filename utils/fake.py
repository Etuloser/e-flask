"""
github repo:
https://github.com/joke2k/faker

install:
pip install faker

func:
name()
email()
"""
from faker import Faker


class Fake:
    def __init__(self):
        self.fake = Faker(locale='zh_CN')
