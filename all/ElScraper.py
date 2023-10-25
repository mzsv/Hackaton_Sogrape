# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ElScraper.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: amenses- <amenses-@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/24 18:25:56 by amenses-          #+#    #+#              #
#    Updated: 2023/10/24 23:18:47 by amenses-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup
from datetime import date
import requests
import pandas as pd
import sqlalchemy
class ElScraper:
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
            store_name = soup.find('footer', class_="footer _copy").text.strip()
            store_name = store_name.split(',')[1].split('S.A.')[0].strip()

            # wine name
            wine_name = soup.find('div', class_="page_title").h1.text.strip()

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
            price_value = price.find('div', class_="prices-price _current")
            discount = 0
            if price_value == None:
                price_value = price.find('div', class_="prices-price _offer")
                discount = 1
            price_value = float(price_value.text.strip().split()[0].replace(',', '.'))

            # currency
            price_currency = price.find('span', class_="js-currency").text.strip()

            # capacity
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
                    break
            
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
