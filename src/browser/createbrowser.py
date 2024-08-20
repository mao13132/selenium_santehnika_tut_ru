import logging
import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import getpass

from settings import ACTIVE_WINDOW_BROWSER


class CreatBrowser:

    def __init__(self, name_profile):

        logging.getLogger('selenium').setLevel(logging.ERROR)

        user_system = getpass.getuser()

        options = webdriver.ChromeOptions()

        if not ACTIVE_WINDOW_BROWSER:
            options.add_argument("--headless")

        prefs = {"enable_do_not_track": True}

        options.add_experimental_option("prefs", prefs)

        options.add_argument("--disable-blink-features=AutomationControlled")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        options.add_argument("--disable-infobars")

        options.add_argument("--disable-bundled-ppapi-flash")

        options.add_argument("--disable-application-cache")

        options.add_argument("window-size=1920,939")

        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--disable-gpu")

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('ignore-certificate-errors')
        options.add_argument("--log-level=3")

        experimental_options = {
            'excludeSwitches': ['enable-automation', 'enable-logging'],
            'prefs': {'profile.default_content_setting_values.notifications': 2, 'intl.accept_languages': 'en-US,en'}
        }

        for key, value in experimental_options.items():
            options.add_experimental_option(key, value)

        path_driver = ChromeDriverManager().install()

        try:
            path_split = path_driver.split('/')

            path_driver = f"{path_split[0]}{os.sep}chromedriver.exe"
        except Exception as es:
            print(f'Не могу получить адрес google драйвера "{es}"')

        self.driver = webdriver.Chrome(service=Service(path_driver), options=options)

        try:
            browser_version = self.driver.capabilities['browserVersion']
            driver_version = self.driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
            print(f"Браузер: {browser_version} драйвер: {driver_version}\n")
        except:
            print(f'Не получилось определить версию uc браузера')