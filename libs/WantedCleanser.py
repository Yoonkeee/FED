import json
from typing import *


class Cleanser:

    raw_data: dict = {}
    cleansed_data: dict = {}
    tech_stacks = ['react', 'javascript', 'python', 'java', 'kotlin', 'RDBMS']

    def __init__(self, raw_data: dict):
        if raw_data['is_valid']:
            self.raw_data = raw_data
        else:
            raise Exception(raw_data)
        self.cleanse()

    def cleanse(self):
        for data in self.raw_data['data']['requirements'].split('\n'):
            print(data)
            for tech_stack in self.tech_stacks:
                if tech_stack in data:
                    self.cleansed_data[tech_stack] = True



