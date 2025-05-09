from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Caminho para o ChromeDriver (ajuste se necessário)
# Você pode baixar em: https://chromedriver.chromium.org/downloads
service = Service()

# Inicializa o navegador
driver = webdriver.Chrome(service=service)

try:
    # Abre o site hospedado na Vercel
    driver.get("https://meu-portfolio-qrxh.vercel.app/")
    time.sleep(3)  # Aguarda 3 segundos para a página carregar

    # Testa se o título da página contém "React App"
    assert "React App" in driver.title
    print("✅ Página carregada com sucesso e título validado!")

    # Testa se existe um elemento com a tag H1 (se necessário, altere para outro elemento)
    header = driver.find_element(By.TAG_NAME, "h1")
    print("✅ H1 encontrado com texto:", header.text)

except AssertionError:
    print("❌ O título da página não está como esperado.")
except Exception as e:
    print("❌ Ocorreu um erro durante o teste:", e)
finally:
    driver.quit()
