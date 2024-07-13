from webdriver_setup import WebDriverChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Criando função para clicar nos botão 
def click_button(chrome, url):
    xpath = '//*[@class="btn btn-actions"]' #procure o path do q for ser clicado
    try:
        chrome.driver.get(url)
        buttons = len(chrome.driver.find_elements(By.XPATH, xpath))
        if buttons > 0:
            for item in range(0, buttons):
                elem = chrome.driver.find_element(By.XPATH, f'{xpath}')
                chrome.driver.execute_script("arguments[0].click();", elem)
                sleep(0.3)
    except Exception as e:
        print(f"An error occurred while processing URL {url}: {e}")

def run_script():
    chrome = WebDriverChrome()
    try:
        # entrando no site e logando 
        base_url = 'https://examplo.com.br/'

        chrome.driver.get(base_url)
        
        WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="LoginForm[username]"]')))
        chrome.driver.find_element(By.XPATH, '//*[@name="LoginForm[username]"]').send_keys('Usuario')

        WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="LoginForm[password]"]')))
        chrome.driver.find_element(By.XPATH, '//*[@name="LoginForm[password]"]').send_keys('senhaforte')

        WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@type="submit"]')))
        buttonLogin = chrome.driver.find_element(By.XPATH, '//*[@type="submit"]')

        chrome.driver.execute_script("arguments[0].click();", buttonLogin)
        # -----------------------------------------------------

        # se tiver recaptcha resolver manualmente e dar enter no console
        try:
            recaptcha = WebDriverWait(chrome.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "g-recaptcha"))
            )
            if recaptcha:
                print("Please solve the reCAPTCHA manually and press Enter...")
                input()
                
            WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="LoginForm[username]"]')))
            chrome.driver.find_element(By.XPATH, '//*[@name="LoginForm[username]"]').send_keys('Usuario')

            WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="LoginForm[password]"]')))
            chrome.driver.find_element(By.XPATH, '//*[@name="LoginForm[password]"]').send_keys('senhadforte')

            WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@type="submit"]')))
            buttonLogin = chrome.driver.find_element(By.XPATH, '//*[@type="submit"]')

            chrome.driver.execute_script("arguments[0].click();", buttonLogin)
        except Exception as e:
            print("No reCAPTCHA found, proceeding with login...")
        # -----------------------------------------------------

        # Criando lista de urls para loopar com a função de clickar nos botões
        base_url = 'https://exemplo.com.br/orders/'
        urls = [f'{base_url}{i}' for i in range(1, 26)]
        # print(urls)
        for url in urls:
            click_button(chrome, url)
            sleep(1)
        # ----------------------------------------------------
    finally:
        print("ALL REFELLED")
        chrome.close()

if __name__ == '__main__':
    run_script()