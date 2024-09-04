# Projeto 3 - Discursos de Vargas

# Baixar pelo menos 20 discursos de Getulio Vargas em pdf em todos os anos disponíveis.
# Colocar os PDFs em um diretório chamado "discursos_vargas" e zipar.
# Enviar pelo Teams o código (já iniciado aqui) e o zip.

# Valor: 1,0

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

url = 'http://www.biblioteca.presidencia.gov.br/presidencia/presidencia/ex-presidentes/getulio-vargas'

options = Options()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
