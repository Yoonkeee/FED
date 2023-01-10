import json
import requests
from typing import *
from bs4 import BeautifulSoup

# input = url : str
# output = result : dict { 'is_valid': bool, 'data': dict or str }


class Parser:
    # 86252
    post_id: str = ''
    url: str = "https://www.wanted.co.kr"
    request: requests = None
    bs: BeautifulSoup = None
    head_content: str = ''
    main_content: str | dict | BeautifulSoup = ''
    raw_data: dict = {}
    raw_data_desc: dict = {
        'main_tasks': '주요 업무',
        'requirements': '자격 요건',
        'jd': '본문 내용',
        # 'advantages': '우대 사항',  # parse from 'jd'
        # 'walfare': '혜택 및 복지',  # parse from 'jd'
        'company_name': '회사명',
        'company_logo_url': '로고 이미지',
        'address': '위치',
        'due_time': '마감일',
        'origin_link': '원 공고 링크',  # 직접 추가하는 data
        # 'hashtag': '해시태그',  # parse from 'jd'
    }
    is_valid: bool = False
    verify_keywords: dict = {  # verify whether raw data is valid or not. keywords must be in raw data
        'main_tasks': '주요 업무',
        'requirements': '자격 요건',
        'jd': '본문 내용',
        # 'advantages': '우대 사항',  # parse from 'jd'
        # 'walfare': '혜택 및 복지',  # parse from 'jd'
        'company_name': '회사명',
        'address': '위치',
    }
    not_valid_keys: str = ''

    def __init__(self, post_id: str | int) -> None:
        self.post_id = str(post_id)
        self.url += "/wd/" + self.post_id
        for key in self.raw_data_desc.keys():
            self.raw_data[key] = ''  # 1
        self.get_request()
        self.set_content()
        self.parse_data()
        self.raw_data['origin_link'] = self.url
        self.verify_data()

    def get_request(self) -> None:
        self.request = requests.get(self.url)

    def set_content(self) -> None:
        self.bs = BeautifulSoup(self.request.content, "html.parser",
                                from_encoding="utf-8")
        self.head_content = self.bs.find("script", type="application/ld+json")
        self.main_content = self.bs.find("script", type="application/json")
        self.main_content = json.loads(self.main_content.contents[0])
        self.main_content = self.main_content['props']['pageProps']['head'][self.post_id]

    def parse_data(self) -> None:
        self.raw_data['post_id'] = self.post_id
        for key, val in self.main_content.items():
            self.raw_data[key] = val

    def verify_data(self) -> None:
        for keyword in self.verify_keywords.keys():
            if keyword not in self.raw_data.keys():
                self.not_valid_keys = f'{self.url}에서 키워드 {keyword}가 파싱되지 않음.'
                return None
        self.is_valid = True

    def get_raw_data(self) -> dict:
        if self.is_valid:
            result = {
                'is_valid': True,
                'data': self.raw_data
            }
        else:
            result = {
                'is_valid': False,
                'data': self.not_valid_keys,
            }
        return result

    def get_raw_data_info(self) -> dict:
        return self.raw_data_desc
