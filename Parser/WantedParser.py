import json
import requests
from bs4 import BeautifulSoup


class Parser:
    # 86252
    recruit_id: str = ''
    url: str = "https://www.wanted.co.kr"
    request: requests = None
    bs: BeautifulSoup = None
    head_content: str = ''
    main_content: str = ''
    raw_data: dict = {}
    raw_data_desc: dict = {
        'main_tasks': '주요 업무',
        'requirements': '자격 요건',
        'jd': '본문 내용',
        # 'advantages': '우대 사항',
        # 'walfare': '혜택 및 복지',
        'company_name': '회사명',
        'logo_img': '로고 이미지',
        'address': '위치',
        'due_time': '마감일',
        'orgin_link': '원 공고 링크',  # 직접 추가하는 data
        # 'hashtag': '해시태그',
    }

    def __init__(self, recruit_id: int) -> None:
        self.recruit_id = str(recruit_id)
        self.url += "/wd/" + self.recruit_id
        for key in self.raw_data_desc.keys():
            self.raw_data[key] = ''  # 1
        self.get_request()
        self.set_content()
        self.parse_data()

    def get_request(self) -> None:
        self.request = requests.get(self.url)

    def set_content(self) -> None:
        self.bs = BeautifulSoup(self.request.content, "html.parser",
                                from_encoding="utf-8")
        self.head_content = self.bs.find("script", type="application/ld+json")
        self.main_content = self.bs.find("script", type="application/json")
        self.main_content = json.loads(self.main_content.contents[0])
        self.main_content = self.main_content['props']['pageProps']['head'][
            self.recruit_id]

    def parse_data(self) -> None:
        for key, val in self.main_content.items():
            self.raw_data[key] = val

    def go(self) -> None:
        for key in self.raw_data_desc.keys():
            self.raw_data[key] = ''  # 1
        self.get_request()
        self.set_content()
        self.parse_data()
        self.raw_data['orgin_link'] = self.url

    def get_raw_data(self) -> dict:
        # self.go()
        return self.raw_data
