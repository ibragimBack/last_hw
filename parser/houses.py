import httpx
from parsel import Selector
from pprint import pprint

MAIN_URL = "https://www.house.kg/snyat"
BASE_URL = "https://www.house.kg"

data = []

def get_html(url):
    response = httpx.get(url)
    return Selector(response.text)

def get_title(html):
    title = html.css('title::text').get()
    return title

def get_houses_links(html):
    houses = html.css('.profile-navigation a::attr(href)').getall()
    links = list(map(lambda x: BASE_URL + x, houses))
    return links

def clean_text(text: str):
    if text is None:
        return ''
    text = ''.join(text.split())
    return text.strip().replace('\t', '').replace('\n', '')

def price_to_int(price: str):
    result_price = ''
    for i in price:
        if i.isdigit():
            result_price+=i
    return int(result_price)

def get_house_data(html):
    houses = html.css('.main-wrapper')
    houses_list = []
    for house in houses:
        house_data = {}
        house_data['title'] = clean_text(house.css('.title a::text').get())
        house_data['price'] = price_to_int(clean_text(house.css('.price::text').get()))
        house_data['address'] = clean_text(house.css('.address::text').getall()[1])
        houses_list.append(house_data)
    return houses_list

def get_houses():
    houses = []
    for page in range(1, 4):
        url = f'{MAIN_URL}?page={page}'
        html = get_html(url)
        houses.extend(get_house_data(html))
    return houses

if __name__ == '__main__':
    html = get_html(MAIN_URL)
    title = get_title(html)
    # pprint(title)
    links = get_houses_links(html)
    # pprint(links)
    houses_data = get_house_data(html)
    # pprint(houses_data)
    houses = get_houses()
