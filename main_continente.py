# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main_continente.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: amenses- <amenses-@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/24 21:27:44 by amenses-          #+#    #+#              #
#    Updated: 2023/10/25 01:09:59 by amenses-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import ContiScraper as conti
import time
import datetime

urls = {
    'mateus_rose_75' : 'https://www.continente.pt/produto/mateus-medium-sweet-vinho-rose-mateus-3777012.html',
    'mateus_rose_37' : 'https://www.continente.pt/produto/mateus-vinho-rose-mateus-2103486.html',
    'mateus_rose_150' : 'https://www.continente.pt/produto/mateus-vinho-rose-mateus-2922551.html',
    'mateus_sparkling' : 'https://www.continente.pt/produto/mateus-sparkling-espumante-rose-bruto-mateus-4342301.html',
    'trinca_bolotas' : 'https://www.continente.pt/produto/trinca-bolotas-regional-alentejano-vinho-tinto-trinca-bolotas-5471317.html',
    'papa_figos' : 'https://www.continente.pt/produto/papa-figos-doc-douro-vinho-branco-papa-figos-6274693.html',
    'discount_example' : 'https://www.continente.pt/produto/cancellus-premium-doc-douro-vinho-tinto-cancellus-5717619.html' 
}

conti_scraper = conti.ContiScraper(urls)
conti_scraper.scrape()
timestamp = datetime.datetime.fromtimestamp(int(time.time())).strftime('_%Y%m%d_%H%M%S')
conti_scraper.save_to_csv('continente' + timestamp + '.csv')
