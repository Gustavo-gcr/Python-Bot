from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

# Configuração do WebDriver
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def search_chatgpt(query):
    driver.get('https://chat.openai.com')
    time.sleep(10)  # Aguardar o carregamento da página e o login, se necessário

    search_box = driver.find_element("css selector", 'textarea')  # Atualize o seletor conforme necessário
    search_box.send_keys(query)
    search_box.send_keys('\n')  # Enviar a tecla Enter
    time.sleep(10)  # Aguardar a resposta carregar

    # Capturar o resultado
    response = driver.find_element("css selector", 'div.result-class').text  # Atualize o seletor conforme necessário
    return response

def search_gemini(query):
    driver.get('https://gemini.google.com/app')
    time.sleep(10)  # Aguardar o carregamento da página e o login, se necessário

    search_box = driver.find_element("css selector", 'input')  # Atualize o seletor conforme necessário
    search_box.send_keys(query)
    search_box.send_keys('\n')  # Enviar a tecla Enter
    time.sleep(10)  # Aguardar a resposta carregar

    # Capturar o resultado
    response = driver.find_element("css selector", 'div.result-class').text  # Atualize o seletor conforme necessário
    return response

def search_copilot(query):
    driver.get('https://copilot.microsoft.com/')
    time.sleep(10)  # Aguardar o carregamento da página e o login, se necessário

    search_box = driver.find_element("css selector", 'input')  # Atualize o seletor conforme necessário
    search_box.send_keys(query)
    search_box.send_keys('\n')  # Enviar a tecla Enter
    time.sleep(10)  # Aguardar a resposta carregar

    # Capturar o resultado
    response = driver.find_element("css selector", 'div.result-class').text  # Atualize o seletor conforme necessário
    return response

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query', '')
    responses = {
        'chatgpt': search_chatgpt(query),
        'gemini': search_gemini(query),
        'copilot': search_copilot(query)
    }
    return jsonify(responses)
if __name__ == '__main__':
    app.run(debug=True)
