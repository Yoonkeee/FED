import json
from typing import *


class Cleanser:

    raw_data: dict = {}
    cleansed_data: dict = {}
    tech_stacks = ['react', 'javascript', 'python', 'java', 'kotlin', 'RDBMS', 'spring',
                   'vue.js', 'angular', 'node.js', 'django', 'flask', 'spring boot',
                   'swift', 'flutter', 'objective-c', 'go', 'typescript', 'ruby', 'php',
                   'c++', 'c#', 'scala', 'rust', 'haskell', 'erlang', 'elixir',
                   'git', 'docker', 'jenkins', 'kubernetes', 'aws', 'gcp', 'azure',
                   'redis', 'mongodb', 'mysql', 'postgresql', 'oracle', 'mariadb',
                   'nosql']

    def __init__(self, raw_data: dict):
        self.raw_data, self.cleansed_data = {}, {}
        if raw_data['is_valid']:
            self.raw_data = raw_data
        else:
            raise Exception(raw_data)
        self.cleanse()

    def cleanse(self):
        for data in self.raw_data['data']['requirements'].split('\n'):
            # print(data)
            for tech_stack in self.tech_stacks:
                if tech_stack in data.lower():
                    self.cleansed_data[tech_stack] = True



