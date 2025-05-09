from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()

driver = webdriver.Chrome(service=service)

try:
   
    driver.get("https://meu-portfolio-qrxh.vercel.app/")
    time.sleep(3)  # Aguarda 3 segundos para a página carregar

  
    assert "React App" in driver.title
    print("✅ Página carregada com sucesso e título validado!")

  
    header = driver.find_element(By.TAG_NAME, "h1")
    print("✅ H1 encontrado com texto:", header.text)

except AssertionError:
    print("❌ O título da página não está como esperado.")
except Exception as e:
    print("❌ Ocorreu um erro durante o teste:", e)
finally:
    driver.quit()
