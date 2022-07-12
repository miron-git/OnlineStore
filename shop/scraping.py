import requests
from bs4 import BeautifulSoup
import random
from transliterate import translit # транслитерация слага
from django.utils.text import slugify # создание слагов
 

def scraping():
    '''Скрейпинг'''

    URL_SCRAPING = 'https://dynamics.com.ru/production' # url страницы продукции
    resp = requests.get(URL_SCRAPING, timeout=5.0) # получаем код html страницы
    img_url = 'https://dynamics.com.ru' # url для изображения
    if resp.status_code != 200: 
        raise Exception('Error')
    text = resp.text

    soup = BeautifulSoup(text, 'html.parser')
    blocks = soup.select(".productionItem") # получаем список товаров по селектору productionItem

    data_list=[]

    for block in blocks:
        data = {}

        name = block.select_one('.title').get_text(strip=True) # имя по селектору title, strip=True - удаляем пробелы
        data['name'] = name

        description = block.select_one('.desc').get_text(strip=True)
        data['description'] = description

        image = img_url + block.select_one('img')['src'] # url изображения, по img и атрибуту scr
        data['image'] = image

        price = random.randint(50000,100000) # т.к на сайте цены по запросу, ради теста ставим рандом
        data['price'] = price

        slug = slugify(translit(name, language_code='ru', reversed=True)) # создаем слаг из поля name
        data['slug'] = slug
        
        data_list.append(data)

    return data_list    
