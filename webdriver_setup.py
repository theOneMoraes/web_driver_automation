# webdriver_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from subprocess import CREATE_NO_WINDOW

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
            chrome_options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.set_page_load_timeout(10)

    def close(self):
        self.driver.quit()
