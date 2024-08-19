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

        options.add_argument(
            f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0 (Edition Yx 05)")

        if not ACTIVE_WINDOW_BROWSER:
            options.add_argument("--headless")

        platform_to_os = platform.system()

        if platform_to_os == "Linux":
            path_dir = (f'/Users/{user_system}/Library/Application Support/Google/Chrome/{name_profile}')
        else:
            path_dir = (f'C:\\Users\\{user_system}\\AppData\\Local\\Google\\Chrome\\User Data\\{name_profile}')

        options.add_argument(f"user-data-dir={path_dir}")

        prefs = {"enable_do_not_track": True}
        options.add_experimental_option("prefs", prefs)

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-infobars")
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disable-in-process-stack-traces")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--output=/dev/null')
        options.add_argument("--log-level=3")

        options.add_argument("--disable-extensions")
        options.add_argument("--disable-application-cache")
        options.add_argument(f"start-maximized")

        experimental_options = {
            'excludeSwitches': ['enable-automation', 'enable-logging'],
            'prefs': {'profile.default_content_setting_values.notifications': 2, 'intl.accept_languages': 'en-US,en'}
        }

        prefs = {"profile.managed_default_content_settings.images": 0}
        options.add_experimental_option("prefs", prefs)

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

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            'source': '''
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
                  '''
        })
