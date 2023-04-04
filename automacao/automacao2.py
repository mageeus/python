from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Importando as bibliotecas necessárias
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# #puxando o driver mais atual
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.pastebin.com")

# area_texto = navegador.find_element(By.ID, "postform-text")
# area_texto.send_keys("oi")

#esse e o de cima fazem a mesma coisa
navegador.find_element(By.ID, "postform-text").send_keys("ola")


# barra_pesquisa.send_keys("automação")
# barra_pesquisa.send_keys(Keys.RETURN)

while(True):
    pass


navegador.close()
