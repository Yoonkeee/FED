from typing import *
import requests
import json
from bs4 import BeautifulSoup


class IdGenerator:
    url_params: dict = {
        'tag_type_ids': '518',
        'job_sort': 'company.response_rate_order',
        'locations': 'all',
        'years': '-1'
    }
    # url = "https://www.wanted.co.kr/api/v4/jobs?1670145066301&country=kr&tag_type_ids=518&job_sort=company.response_rate_order&locations=all&years=-1"
    url: str = "https://www.wanted.co.kr/api/v4/jobs?1670145066301&country=kr"
    recruit_ids: List[str] = []
    offset: int = 0
    limit_size: int = 50
    load_size: int = 10

    def __init__(self, offset: int = 0, limit_size: int = 50, load_size: int = 10):
        self.offset = offset
        self.limit_size = limit_size
        self.load_size = load_size
        for key, val in self.url_params.items():
            self.url += f'&{key}={val}'

    def get_id_list(self) -> list:
        more_id_exist: bool = True

        while self.offset < self.limit_size:
            request = requests.get(self.url + f"&limit={self.load_size}&offset={self.offset}")
            soup = BeautifulSoup(request.text, "html.parser")
            loaded_data = json.loads(soup.text)
            if loaded_data["data"]:
                for data in loaded_data["data"]:
                    self.recruit_ids.append(str(data["id"]))
                self.offset += self.load_size
            else:
                break

        return self.recruit_ids
