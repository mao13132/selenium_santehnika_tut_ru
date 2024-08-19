import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.business.full_load_page.full_load_page import loop_full_load_page


class LoadPage:
    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.source_name = 'SantehnikaTut'

    def load_page(self, url):
        try:
            self.driver.get(url)
            return True
        except:
            return False

    def check_load_page(self, _xpatch):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, _xpatch)))
            return True
        except:
            return False

    def loop_load_page(self, _xpatch):

        count = 0

        count_over = 20

        self.driver.set_page_load_timeout(15)

        while True:

            count += 1

            if count >= count_over:
                print(f'Не смог открыть "{_xpatch}"')
                return False

            start_page = self.load_page(self.url)

            if not start_page:
                time.sleep(5)
                continue

            loop_full_load_page(self.driver)

            check_page = self.check_load_page(_xpatch)

            if not check_page:

                try:

                    self.driver.refresh()
                except:
                    pass

                continue

            return True
