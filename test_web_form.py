from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

def test_envio_com_sucesso():
   service = FirefoxService(executable_path=GeckoDriverManager().install())
   driver = webdriver.Firefox(service=service)
   driver.get('http://localhost:8000/index.html')
   
   driver.find_element(By.ID, 'nome').send_keys('Maria da Silva')
   driver.find_element(By.ID, 'mensagem').send_keys('Formulário enviado com sucesso!')
   driver.find_element(By.ID, 'enviar').click
   
   time.sleep(1)
   
   resultado = driver.find_element(By.ID, 'resultado').test 
   assert 'Obrigado, Maria da Silva' in resultado
   
   driver.quit()
   
def test_envio_com_falha():
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get('http://localhost:8000/index.html')

    driver.find_element(By.ID, 'nome').send_keys('Mensagem sem nome.')
    driver.find_element(By.ID, 'enviar').click()

    time.sleep(1)  

   
    resultado = driver.find_element(By.ID, 'resultado').text

    assert 'Preencha todos os campos!' in resultado

    driver.quit()
