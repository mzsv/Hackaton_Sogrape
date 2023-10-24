# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: amenses- <amenses-@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/24 18:25:45 by amenses-          #+#    #+#              #
#    Updated: 2023/10/24 23:44:19 by amenses-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import ElScraper as el
import time
import datetime

urls = {
    'mateus_rose_75' : 'https://www.elcorteingles.pt/supermercado/0105218714000033-mateus-vinho-rose-garrafa-75-cl/',
    'mateus_rose_37' : 'https://www.elcorteingles.pt/supermercado/0105218714000074-mateus-vinho-rose-garrafa-375-cl/',
    'mateus_rose_150' : 'https://www.elcorteingles.pt/supermercado/0105218714000041-mateus-vinho-rose-garrafa-15-l/',
    'mateus_sparkling' : 'https://www.elcorteingles.pt/supermercado/0105218731401859-mateus-espumante-sparkling-rose-bruto-garrafa-75-cl/',
    'trinca_bolotas' : 'https://www.elcorteingles.pt/supermercado/0105218722001098-trinca-bolotas-vinho-tinto-regional-do-alentejo-garrafa-75-cl/',
    'papa_figos' : 'https://www.elcorteingles.pt/supermercado/0105218705602987-papa-figos-vinho-branco-do-douro-garrafa-75-cl/',
    'discount_example' : 'https://www.elcorteingles.pt/supermercado/0105218716006228-vinha-da-urze-vinho-tinto-do-douro-grande-reserva-garrafa-75-cl/' 
}

el_scraper = el.ElScraper(urls)
el_scraper.scrape()
timestamp = datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y%m%d%H%M%S')
el_scraper.save_to_csv('elcorteingles' + timestamp + '.csv')
