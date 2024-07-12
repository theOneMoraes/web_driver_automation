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
        sleep(5)
        # create element related to the text box #
        buttons = chrome.driver.find_elements(By.XPATH, '//*[@aria-label="Refill"]')
        # Click each button
        for button in buttons:
            button.click()
            # Optionally, add a sleep time to wait for any resulting actions to complete
            sleep(2)  # Adjust the sleep time as necessary

        # Delay to observe actions
        sleep(10)
    except Exception as e:
        print(f"An error occurred while processing URL {url}: {e}")


def main ():
    chrome= WebDriverChrome()

    try:
        # Create a list of URLs to visit
        base_url = 'https://www.example.com/page'
        urls = [f'{base_url}{i}' for i in range(1, 50)]

        for url in urls:
            click_all_buttons_order(url)
    finally:
        chrome.close()

