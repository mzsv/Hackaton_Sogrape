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
import sqlalchemy

class ContiScraper:
    def __init__(self, urls):
        self.urls = urls
        self.data = pd.DataFrame(columns=['store_name', 'wine_name_mask', 'wine_name', 'price', 'price_currency', 'discount', 'capacity', 'scraping_date', 'location', 'harvest_year'])
    
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

            # wine name mask
            if (wine_name.find('Espumante') != -1):
                wine_name_mask = 'Mateus Sparkling Rose'
            elif (wine_name.find('Papa Figos') != -1):
                wine_name_mask = 'Papa Figos Branco'
            elif (wine_name.find('Vinho Rosé') != -1):
                wine_name_mask = 'Mateus Rose'
            elif (wine_name.find('Trinca Bolotas') != -1):
                wine_name_mask = 'Trinca Bolotas Tinto'
            else:
                wine_name_mask = 'default'

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

            # add capacity to wine name mask
            wine_name_mask += ' ' + str(capacity_value) + 'L'

            # location
            location = "Portugal"

            # harvest year
            year = 0

            # add data to the dataframe
            new_data = pd.DataFrame({'store_name': store_name, 'wine_name_mask' : wine_name_mask, 'wine_name': wine_name, 'price': price_value, 'price_currency': price_currency, 'discount': discount, 'capacity': capacity_value, 'scraping_date': today, 'location': location, 'harvest_year': year}, index=[0])
            if not new_data.isnull().values.all():
                self.data = pd.concat([self.data, new_data], ignore_index=True)

    def save_to_sql(self, filename, connection_string):
        engine = sqlalchemy.create_engine(connection_string)
        self.data.to_sql(filename, engine, index=False, if_exists='append')
