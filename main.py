from bs4 import BeautifulSoup
import sqlite3
import requests
import chardet
import data
import re

cuentos = []
all_words = {}




url_base = "https://ciudadseva.com/"
#autor = "autor/jorge-luis-borges/cuentos/"
#autor = "autor/horacio-quiroga/cuentos/"
autor = "/autor/mario-benedetti/cuentos/"

hdr = {'User-Agent': 'Mozilla/5.0'}


def exist(w):
    size = str(len(w))
    tables = data.getTablesNames()
    if  not "words_"+size in tables:
        return False

    all_words['i'+size] = data.getwords(w)
    return w.lower().strip() in all_words['i'+size]


def getwords(url):
    cuento_req = url
    cuento_page = requests.get(cuento_req,headers=hdr)
    cuento_soup = BeautifulSoup(cuento_page.content, 'html.parser')
    coding = chardet.detect(cuento_page.content).get('encoding')  

    parrafos = cuento_soup.find_all('p')

    for p in parrafos:
        for w in p.text.split(' '):
            x = re.search("\W", w)
            if x:
                continue
            if(not exist(w)):
                print(w)
                data.SaveWord(w)





_req = url_base + autor
_page = requests.get(_req,headers=hdr)
soup = BeautifulSoup(_page.content, 'html.parser')
coding = chardet.detect(_page.content).get('encoding')

urls =  soup.find_all('li',{'class','text-center'})

for url in urls:
    cuentos.append(url.find('a')['href'])
    getwords(url.find('a')['href'])