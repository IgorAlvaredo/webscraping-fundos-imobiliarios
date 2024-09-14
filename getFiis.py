import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# A classe Service é usada para iniciar uma instância do Chrome WebDriver
service = Service()

# webdriver.ChromeOptions é usado para definir a preferência para o brower do Chrome
options = webdriver.ChromeOptions()

# Inicia-se a instância do Chrome WebDriver com as definidas 'options' e 'service'
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.fundsexplorer.com.br/ranking'

driver.get(url)

arquivo = 'fiis.csv'

csv_writer = csv.writer(open(arquivo, 'w'))

table = driver.find_elements(By.TAG_NAME, 'tr')
tableHeader = driver.find_elements(By.TAG_NAME, 'th')
tableData = driver.find_elements(By.TAG_NAME, 'td')

with open(arquivo, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    
    # Localizar os elementos da tabela
    table = driver.find_elements(By.TAG_NAME, 'tr')

    # Extrair e escrever os cabeçalhos
    headers = []
    for th in table[0].find_elements(By.TAG_NAME, 'th'):
        headers.append(th.text)
    if headers:
        print("Inserindo cabeçalhos: {}".format(','.join(headers)))
        csv_writer.writerow(headers)  # Escrever cabeçalhos no CSV

    # Extrair e escrever os dados das linhas
    for tr in table[1:]:  # Pular a primeira linha (cabeçalhos)
        data = []
        for td in tr.find_elements(By.TAG_NAME, 'td'):
            data.append(td.text)
        if data:
            print("Inserindo dados da tabela: {}".format(','.join(data)))