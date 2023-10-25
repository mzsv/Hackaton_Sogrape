import ContiScraper as conti
import GarraScraper as garra
import ElScraper as el
import time
import datetime

urls_conti = {
    'mateus_rose_75' : 'https://www.continente.pt/produto/mateus-medium-sweet-vinho-rose-mateus-3777012.html',
    'mateus_rose_37' : 'https://www.continente.pt/produto/mateus-vinho-rose-mateus-2103486.html',
    'mateus_rose_150' : 'https://www.continente.pt/produto/mateus-vinho-rose-mateus-2922551.html',
    'mateus_sparkling' : 'https://www.continente.pt/produto/mateus-sparkling-espumante-rose-bruto-mateus-4342301.html',
    'trinca_bolotas' : 'https://www.continente.pt/produto/trinca-bolotas-regional-alentejano-vinho-tinto-trinca-bolotas-5471317.html',
    'papa_figos' : 'https://www.continente.pt/produto/papa-figos-doc-douro-vinho-branco-papa-figos-6274693.html',
}

urls_el = {
    'mateus_rose_75' : 'https://www.elcorteingles.pt/supermercado/0105218714000033-mateus-vinho-rose-garrafa-75-cl/',
    'mateus_rose_37' : 'https://www.elcorteingles.pt/supermercado/0105218714000074-mateus-vinho-rose-garrafa-375-cl/',
    'mateus_rose_150' : 'https://www.elcorteingles.pt/supermercado/0105218714000041-mateus-vinho-rose-garrafa-15-l/',
    'mateus_sparkling' : 'https://www.elcorteingles.pt/supermercado/0105218731401859-mateus-espumante-sparkling-rose-bruto-garrafa-75-cl/',
    'trinca_bolotas' : 'https://www.elcorteingles.pt/supermercado/0105218722001098-trinca-bolotas-vinho-tinto-regional-do-alentejo-garrafa-75-cl/',
    'papa_figos' : 'https://www.elcorteingles.pt/supermercado/0105218705602987-papa-figos-vinho-branco-do-douro-garrafa-75-cl/',
}

urls_garra = {
    'mateus_rose_75' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-rose-mateus-75-cl/item_10807.html?id=36&cat=0&pc=1',
    'mateus_rose_37' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-rose-mateus-37-cl/item_10806.html?id=36&cat=0&pc=1',
    'mateus_rose_150' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-rose-mateus-1.5-l/item_10808.html?id=36&cat=0&pc=1',
    'mateus_rose_25' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-rose-mateus-25-cl/item_10805.html?id=36&cat=0&pc=1',
    'mateus_sparkling' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/espumante-mateus-rose-75-cl/item_1127.html?id=36&cat=0&pc=1',
    'trinca_bolotas_75' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-tinto-trinca-bolotas-75-cl/item_10039.html?id=36&cat=0&pc=1',
    'trinca_bolotas_150' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-tinto-trinca-bolotas-1.5-l/item_10041.html?id=36&cat=0&pc=1',
    'trinca_bolotas_500' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-tinto-trinca-bolotas-5-l/item_10042.html?id=36&cat=0&pc=1',
    'papa_figos' : 'https://www.garrafeirasoares.pt/pt/portugal/vinhos/vinho-branco-douro-papa-figos-75-cl/item_10769.html?id=36&cat=0&pc=1',
}

conti_scraper = conti.ContiScraper(urls_conti)
conti_scraper.scrape()
# timestamp = datetime.datetime.fromtimestamp(int(time.time())).strftime('_%Y%m%d_%H%M%S')
connection_string = 'sqlite:///hackawine.db'
conti_scraper.save_to_sql('hackawine_table', connection_string)

el_scraper = el.ElScraper(urls_el)
el_scraper.scrape()
# timestamp = datetime.datetime.fromtimestamp(int(time.time())).strftime('_%Y%m%d_%H%M%S')
el_scraper.save_to_sql('hackawine_table', connection_string)

garra_scraper = garra.GarraScraper(urls_garra)
garra_scraper.scrape()
# timestamp = datetime.datetime.fromtimestamp(int(time.time())).strftime('_%Y%m%d_%H%M%S')
garra_scraper.save_to_sql('hackawine_table', connection_string)
