from selenium import webdriver
from selenium.webdriver.common.by import By
from subprocess import CREATE_NO_WINDOW
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


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

def click_all_buttons_order(url):
    try:
        # open the url #
        chrome.driver.get(url)
        # create element related to the text box #
        buttons = chrome.driver.find_elements(By.XPATH, '//*[@aria-label="Refill"]')
        # Click each button
        for button in buttons:
            button.click()
        # Delay to observe actions
        sleep(20)
    except Exception as e:
        print(f"An error occurred while processing URL {url}: {e}")


def main ():
    try:
        base_url = 'https://justanotherpanel.com'

        chrome.driver.get(base_url)
        
        textBox = chrome.driver.find_element(By.XPATH, '//*[@id="username"]')
        textBox.send_keys('miller_')

        textBox = chrome.driver.find_element(By.XPATH, '//*[@id="password"]')
        textBox.send_keys('senhadajust')

        buttonLogin = chrome.driver.find_element(By.XPATH, '//*[@type=submit and @value="Login"]')
        buttonLogin.click()

        sleep(20)
        # Create a list of URLs to visit
        base_url = 'https://justanotherpanel.com/orders/all/'
        urls = [f'{base_url}{i}' for i in range(1, 51)]
        print(urls)
        for url in urls:
            click_all_buttons_order(url)
            sleep(4)
    finally:
        chrome.close()

if __name__ == '__main__':
    chrome = WebDriverChrome()
    main()