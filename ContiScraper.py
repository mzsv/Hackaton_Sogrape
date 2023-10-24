# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ContiScraper.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: amenses- <amenses-@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/24 21:28:29 by amenses-          #+#    #+#              #
#    Updated: 2023/10/24 23:18:26 by amenses-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup
from datetime import date
import requests
import pandas as pd

class ContiScraper:
    def __init__(self, urls):
        self.urls = urls
        self.data = pd.DataFrame(columns=['store_name', 'wine_name', 'price', 'price_currency', 'discount', 'capacity', 'scraping_date', 'location'])
    
    def scrape(self):
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')"}
        today = date.today()

        for product, url in self.urls.items():
            r = requests.get(url, headers=headers)

            # request status
            if (r.status_code == 200):
                print(f'Request for {product} OK')
            else:
                print(f'Request for {wine_name} failed. Status code: {r.status_code}')
                continue

            # extract data from the url
            soup = BeautifulSoup(r.content, 'html5lib')

            # store name
            store_name = soup.find('div', class_="copyright-notice ct-font--opensans-bookitalic").text.strip()
            store_name = store_name.split(',')[0].split()
            store_name = store_name[2] + ' ' + store_name[3] + ' ' + store_name[4]

            # wine name
            wine_name = soup.find('div', class_="product-name-details").h1.text.strip()

            # price
            price = soup.find('div', class_="prices")
            price_value = price.find('span', class_="value")['content']
            discount = 0
            if (price.find('p', class_="pwc-discount-amount") != None):
                discount = 1
            price_value = float(price_value)

            # currency
            price_currency = price.find('span', class_="ct-price-formatted").text.strip()[0]

            # capacity
            capacity = soup.find('div', class_="product-name-details")
            capacity = capacity.find('span', class_="ct-pdp--unit").text.strip()
            capacity = capacity.split()
            capacity_value = float(capacity[-2].replace(',','.'))
            if (capacity[-1] == 'cl'):
                capacity_value = capacity_value / 100

            # location
            location = "default"

            # add data to the dataframe
            new_data = pd.DataFrame({'store_name': store_name, 'wine_name': wine_name, 'price': price_value, 'price_currency': price_currency, 'discount': discount, 'capacity': capacity_value, 'scraping_date': today, 'location': location}, index=[0])
            if not new_data.isnull().values.all():
                self.data = pd.concat([self.data, new_data], ignore_index=True)

    def save_to_csv(self, filename):
        self.data.to_csv(filename, index=False)
