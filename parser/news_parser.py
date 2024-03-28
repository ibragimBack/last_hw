import re

import requests
from bs4 import BeautifulSoup as BS

URL = 'https://24.kg'

HEADERS = {
    'Accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
}


def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_data(html):
    bs = BS(html, 'html.parser')
    items = bs.find_all('div', class_='one')
    news_list = []
    for item in items:
        title = re.sub(r'\s+',  ' ', item.find('div', class_='title').get_text(strip=True))
        time = re.sub(r'\s+', ' ', item.find('div', class_='time').get_text(strip=True))
        news_list.append({'title': title, 'time': time})
    return news_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        news_list_2 = []
        for page in range(1, 2):
            response = get_html('https://24.kg/vlast/', params={'page': page})
            news_list_2.extend(get_data(response.text))
        return news_list_2
    else:
        raise Exception('Ошибка при парсинге')


# print(parsing())
