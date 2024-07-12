from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from subprocess import CREATE_NO_WINDOW
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

# n sei q q faz foi um grande amigo que fez, então se souber um comentário melhor escreva abaixo
# Aqui--
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
        buttons = chrome.driver.find_elements(By.XPATH, '//*[@aria-label="Refill" and @data-bs-original-title="Refill"]')
        # looping de clicks para cada botão achado
        for button in buttons:
            button.click()
    except Exception as e:
        print(f"An error occurred while processing URL {url}: {e}")

def main():
    try:
        # entrando no site e logando 
        base_url = 'https://justanotherpanel.com'

        chrome.driver.get(base_url)

        textBox = chrome.driver.find_element(By.XPATH, '//*[@id="username"]')
        textBox.send_keys('miller_')

        textBox = chrome.driver.find_element(By.XPATH, '//*[@id="password"]')
        textBox.send_keys('senhadajust')

        buttonLogin = chrome.driver.find_element(By.XPATH, '//input[@type="submit" and @value="Login"]')
        buttonLogin.click()
        # -----------------------------------------------------

        # se tiver recaptcha resolver manualmente e dar enter no console
        try:
            recaptcha = WebDriverWait(chrome.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "g-recaptcha"))
            )
            if recaptcha:
                print("Please solve the reCAPTCHA manually and press Enter...")
                input()
                
                textBox = chrome.driver.find_element(By.XPATH, '//*[@id="username"]')
                textBox.send_keys('miller_')

                textBox = chrome.driver.find_element(By.XPATH, '//*[@id="password"]')
                textBox.send_keys('senhadajust')

                buttonLogin = chrome.driver.find_element(By.XPATH, '//input[@type="submit" and @value="Login"]')
                buttonLogin.click()
        except Exception as e:
            print("No reCAPTCHA found, proceeding with login...")
        # -----------------------------------------------------

        # Criando lista de urls para loopar com a função de clickar nos botões
        base_url = 'https://justanotherpanel.com/orders/all/'
        urls = [f'{base_url}{i}' for i in range(1, 51)]
        # print(urls)
        for url in urls:
            click_all_buttons_order(url)
            sleep(2)
        # ----------------------------------------------------
    finally:
        chrome.close()

if __name__ == '__main__':
    chrome = WebDriverChrome()
    main()