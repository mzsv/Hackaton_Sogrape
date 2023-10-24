# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ElScraper.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: amenses- <amenses-@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/24 18:25:56 by amenses-          #+#    #+#              #
#    Updated: 2023/10/24 18:26:46 by amenses-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup
from datetime import date
import requests
import pandas as pd

class ElScraper:
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
            store_name = soup.find('footer', class_="footer _copy").text.strip()
            store_name = store_name.split(',')[1].split('S.A.')[0].strip()

            # wine name
            wine_name = soup.find('div', class_="page_title").h1.text.strip()

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

            # location
            location = "default"

            # add data to the dataframe
            new_data = pd.DataFrame({'store_name': store_name, 'wine_name': wine_name, 'price': price_value, 'price_currency': price_currency, 'discount': discount, 'capacity': capacity_value, 'scraping_date': today, 'location': location}, index=[0])
            self.data = pd.concat([self.data, new_data], ignore_index=True)

    def save_to_csv(self, filename):
        self.data.to_csv(filename, index=False)
