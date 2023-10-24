# building a scraper for wine products from elcorteingles.pt/supermercado/

from bs4 import BeautifulSoup
from datetime import date
import requests

el = {
    'mateus_rose' : 'https://www.elcorteingles.pt/supermercado/0105218714000033-mateus-vinho-rose-garrafa-75-cl/',
    'mateus_sparkling' : 'https://www.elcorteingles.pt/supermercado/0105218731401859-mateus-espumante-sparkling-rose-bruto-garrafa-75-cl/',
    'trinca_bolotas' : 'https://www.elcorteingles.pt/supermercado/0105218722001098-trinca-bolotas-vinho-tinto-regional-do-alentejo-garrafa-75-cl/',
    'papa_figos' : 'https://www.elcorteingles.pt/supermercado/0105218705602987-papa-figos-vinho-branco-do-douro-garrafa-75-cl/',
    'discount' : 'https://www.elcorteingles.pt/supermercado/0105218716006228-vinha-da-urze-vinho-tinto-do-douro-grande-reserva-garrafa-75-cl/' 
}

# html_text = requests.get('https://www.elcorteingles.pt/supermercado/')

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')"}
  
r = requests.get(el['papa_figos'], headers=headers)
# r = requests.get(el, headers=headers)

# response = requests.get(cont_url)

if (r.status_code == 200):
    print('Request OK')
else:
    print('Request failed. Status code: {response.status_code}')
    exit()

# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

store_name = soup.find('footer', class_="footer _copy").text.strip()
store_name = store_name.split(',')[1].split('S.A.')[0].strip()
print("store name:", store_name)

wine_name = soup.find('div', class_="page_title").h1.text.strip()
print("wine name:", wine_name)

price = soup.find('div', class_="prices")
price_value = price.find('div', class_="prices-price _current")
discount = 0
if price_value == None:
    price_value = price.find('div', class_="prices-price _offer")
    discount = 1
price_value = float(price_value.text.strip().split()[0].replace(',', '.'))
print("price:", price_value)
# print(price)
price_currency = price.find('span', class_="js-currency").text.strip()
print("currency:", price_currency)
print("discount:", discount)

capacity = soup.find('div', class_="info")
capacity_value = capacity.find_all('li')
for i in range(len(capacity_value)):
    if "Quantidade" in capacity_value[i].text:
        capacity_value = capacity_value[i].text.split(':')[1]
        if "cl" in capacity_value:
            capacity_value = capacity_value.split()[0]
            capacity_value = float(capacity_value) / 100
        else:
            if "Mililitros" in capacity_value:
                capacity_value = capacity_value.split()[0]
                capacity_value = float(capacity_value) / 1000
        print("capacity:", capacity_value, "l")
        break
# print("capacity:", capacity_value[0].text)
# print("capacity:", capacity_value[1].text.split()[2] + "ml")
# json_data = r.json()

today = date.today()
print("scraping date:", today)

location = "default"
print("location:", location)
# print(json_data)

import pandas as pd

data = {
    'store_name': store_name,
    'wine_name': wine_name,
    'price': price_value,
    'price_currency': price_currency,
    'discount': discount,
    'capacity': capacity_value,
    'scraping_date': today,
    'location': location
}
# save data in a csv file
soup_data = pd.DataFrame(data, index=[0])
soup_data.to_csv('elcorteingles.csv', mode='a', header=False, index=False, encoding='utf-8')
print(pd.__version__)
# soup_data = pd.DataFrame(columns=['store_name', 'wine_name', 'price', 'price_currency', 'discount', 'capacity', 'scraping_date', 'location'])

# print(5+5)
# wine = soup.find('div', class_='product_detail-images')
# wine_name = wine.h1.text.strip()
# wine_price = wine.find('span', class_='product_detail-price').text.strip()
# wine_price = wine_price.replace('€', '')
# wine_price = wine_price.replace(',', '.')
# wine_price = float(wine_price)
# wine_price = round(wine_price, 2)
# wine_price = str(wine_price)
# wine_price = wine_price.replace('.', ',')
# wine_price = wine_price + '€'
# wine_description = wine.find('div', class_='product_detail-description').text.strip()
# print(wine_name)
