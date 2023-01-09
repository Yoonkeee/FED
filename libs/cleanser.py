import re
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
        self.raw_data = {}
        self.cleansed_data = {
            'tech_stacks': {}
        }
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
                    self.cleansed_data['tech_stacks'][tech_stack] = True
        # career = re.search(r'\d+', self.raw_data['data']['position']).extract()
        # if career:
        #     self.cleansed_data['career'] = career
        # else:
        #     self.cleansed_data['career'] = 0

        # setting data
        self.cleansed_data['post_id'] = self.raw_data['data']['post_id']
        self.cleansed_data['start_date'] = self.raw_data['data']['confirm_time']
        # self.cleansed_data['end_date'] = self.raw_data['data']['']
        self.cleansed_data['end_date'] = self.raw_data['data']['confirm_time']  # temporary
        self.cleansed_data['company_id'] = self.raw_data['data']['company_id']
        self.cleansed_data['company_name'] = self.raw_data['data']['company_name']
        # self.cleansed_data['career'] = self.raw_data['data']['']
        self.cleansed_data['career'] = 0  # temporary
        # self.cleansed_data['team_id'] = self.raw_data['data']['']
        # self.cleansed_data['team_name'] = self.raw_data['data']['']
        self.cleansed_data['team_id'] = self.raw_data['data']['post_id']  # temporary
        self.cleansed_data['team_name'] = self.raw_data['data']['post_id']  # temporary
        self.cleansed_data['post_link'] = self.raw_data['data']['origin_link']
        self.cleansed_data['address'] = self.raw_data['data']['location']
