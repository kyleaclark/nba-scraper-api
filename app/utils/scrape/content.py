import requests
from bs4 import BeautifulSoup


def fetch_html_content(url: str) -> bytes:
    result = requests.get(url).content
    return result


def create_soup_instance(content: bytes) -> BeautifulSoup:
    result = BeautifulSoup(content, features='lxml')
    return result
