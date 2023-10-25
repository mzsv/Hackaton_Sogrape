# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main_garrafeira.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: amenses- <amenses-@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/24 23:51:59 by amenses-          #+#    #+#              #
#    Updated: 2023/10/25 01:09:03 by amenses-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import GarraScraper as garra
import time
import datetime

urls = {
    'mateus_rose_75' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-rose-mateus-75-cl/item_10807.html?id=36&cat=0&pc=1',
    'mateus_rose_37' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-rose-mateus-37-cl/item_10806.html?id=36&cat=0&pc=1',
    'mateus_rose_150' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-rose-mateus-1.5-l/item_10808.html?id=36&cat=0&pc=1',
    'mateus_rose_25' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-rose-mateus-25-cl/item_10805.html?id=36&cat=0&pc=1',
    'mateus_sparkling' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/espumante-mateus-rose-75-cl/item_1127.html?id=36&cat=0&pc=1',
    'trinca_bolotas_75' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-tinto-trinca-bolotas-75-cl/item_10039.html?id=36&cat=0&pc=1',
    'trinca_bolotas_150' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-tinto-trinca-bolotas-1.5-l/item_10041.html?id=36&cat=0&pc=1',
    'trinca_bolotas_500' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-tinto-trinca-bolotas-5-l/item_10042.html?id=36&cat=0&pc=1',
    'papa_figos' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-branco-douro-papa-figos-75-cl/item_10769.html?id=36&cat=0&pc=1',
    'discount_example' : 'https://www.garrafeirasoares.pt/pt/espanha/espirituosos/absinto-calavera-rojo-89.9-5-cl/item_9877.html?id=1851&cat=1855&pc=1' 
}

garra_scraper = garra.GarraScraper(urls)
garra_scraper.scrape()
timestamp = datetime.datetime.fromtimestamp(int(time.time())).strftime('_%Y%m%d_%H%M%S')
garra_scraper.save_to_csv('garrafeira' + timestamp + '.csv')
