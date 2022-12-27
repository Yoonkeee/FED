import json
from typing import *


class Cleanser:
    raw_data: dict = {}
    cleansed_data: dict = {}
    # first sieve (back-end tech stacks)
    eratos: list[str] = ['javascript', 'node.js', 'java', 'c++', 'c#', 'python', 'ruby',
                         'go', 'swift', 'kotlin', 'scala', 'rust', 'objective-c']
    # second sieve
    thenes = {}

    def __init__(self, raw_data: dict):
        self.raw_data, self.cleansed_data = {}, {}
        if raw_data['is_valid']:
            self.raw_data = raw_data
        else:
            raise Exception(raw_data)
        self.cleanse()

    def cleanse(self):
        for data in self.raw_data['data']['jd'].split('\n'):
            # print(data)
            for tech_stack in self.eratos:
                if tech_stack in data.lower():
                    self.cleansed_data[tech_stack] = True
