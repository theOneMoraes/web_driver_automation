from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from subprocess import CREATE_NO_WINDOW
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

# A classe WebDriverChrome encapsula a configuração e inicialização de um navegador Chrome com Selenium.
# Ela permite a opção de executar o navegador em modo headless (sem interface gráfica).
class WebDriverChrome:
    def __init__(self, headless=False):
        chrome_service = ChromeService(ChromeDriverManager().install())
        chrome_service.creation_flags = CREATE_NO_WINDOW
        chrome_options = Options()
        chrome_options.use_chromium = True
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        if headless:
            # Used to hide the browser
            chrome_options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        # SET PAGE TIMOUT
        self.driver.set_page_load_timeout(10)
    
    def close(self):
        self.driver.quit()

# Criando função para clicar nos botão
def click_all_buttons_order(url):
    try:
        chrome.driver.get(url)
        buttons = len(chrome.driver.find_elements(By.XPATH, '//*[@class="btn btn-actions"]'))
        if buttons > 0:
            for item in range(0, buttons):
                elem = chrome.driver.find_element(By.XPATH, f'//*[@class="btn btn-actions"]')
                chrome.driver.execute_script("arguments[0].click();", elem)
                sleep(0.5)
    except Exception as e:
        print(f"An error occurred while processing URL {url}: {e}")

def main():
    try:
        # entrando no site e logando 
        base_url = 'https://painelturbo.com/'

        chrome.driver.get(base_url)
        
        WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="LoginForm[username]"]')))
        chrome.driver.find_element(By.XPATH, '//*[@name="LoginForm[username]"]').send_keys('statusbr')

        WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="LoginForm[password]"]')))
        chrome.driver.find_element(By.XPATH, '//*[@name="LoginForm[password]"]').send_keys('senhadoturbo')

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
            chrome.driver.find_element(By.XPATH, '//*[@name="LoginForm[username]"]').send_keys('statusbr')

            WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="LoginForm[password]"]')))
            chrome.driver.find_element(By.XPATH, '//*[@name="LoginForm[password]"]').send_keys('senhadafama')

            WebDriverWait(chrome.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@type="submit"]')))
            buttonLogin = chrome.driver.find_element(By.XPATH, '//*[@type="submit"]')

            chrome.driver.execute_script("arguments[0].click();", buttonLogin)
        except Exception as e:
            print("No reCAPTCHA found, proceeding with login...")
        # -----------------------------------------------------

        # Criando lista de urls para loopar com a função de clickar nos botões
        base_url = 'https://painelturbo.com/orders/'
        urls = [f'{base_url}{i}' for i in range(1, 21)]
        # print(urls)
        for url in urls:
            click_all_buttons_order(url)
            sleep(2)
        # ----------------------------------------------------
    finally:
        print("ALL REFFELLED")
        chrome.close()

if __name__ == '__main__':
    chrome = WebDriverChrome()
    main()