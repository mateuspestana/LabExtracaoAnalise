# Projeto 3 - Deckbox

# Baixar todas os integrantes da FGV Comunicação Rio.
# Salvar em um único Excel, contendo nome, url, bio, foto e cargo de cada integrante.
# Enviar pelo Teams o notebook com o código (já iniciado aqui) e o Excel.

# Valor: 1,0

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

url = 'https://ecmi.fgv.br/corpo-docente'

options = Options()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
