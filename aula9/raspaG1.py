import numpy as np
import pandas as pd 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

from datetime import datetime
import time
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/'

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

print('Acessando a página do G1...')
driver.get(url)

print('Aguardando 3 segundos...')
time.sleep(3)

print('Buscando notícias sobre a Rússia...')
buscador = driver.find_element(By.ID, 'busca-campo')
buscador.send_keys('rússia')
buscador.send_keys(Keys.RETURN)
time.sleep(3)

print('Clicando em "Ver mais"...')

for i in range(10):
    print(f'Clicando em "Ver mais" {i+1} vez(es)...')
    ver_mais = driver.find_element(By.CLASS_NAME, 'pagination__load-more')
    ver_mais.click()
    time.sleep(2)

print('Pegando notícias...')
soup = BeautifulSoup(driver.page_source, 'html.parser')

noticias = soup.find_all('div', {'class': 'widget--info__text-container'})

lista_noticias = []
for noticia in noticias:
    link = noticia.find('a')['href']
    titulo = noticia.find('div', {'class': 'widget--info__title'}).get_text().strip()
    descricao = noticia.find('p').get_text()
    dados = {'link': link, 'titulo': titulo, 'descricao': descricao}
    lista_noticias.append(dados)

print('Salvando notícias...')
df = pd.DataFrame(lista_noticias)
print(df.head())
print(df.shape)
df.to_csv('aula9/noticias_g1.csv', index=False)

print('Fechando navegador...')
driver.quit()