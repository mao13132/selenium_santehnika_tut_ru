# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from selenium.webdriver.common.by import By

from src.business.close_jivo.close_jivo import loop_close_jivo
from src.business.close_popup.close_popup import close_popup
from src.business.mode_get_links.full_load_page.full_load_page import loop_full_load_page
from src.logger._logger import logger_msg


class GetImage:
    def __init__(self, driver):
        self.driver = driver

        self.images = []

    def open_container_images(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@class, 'prod_img')]").click()
        except:
            return False

        return True

    def is_open_container(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@class, 'zoomable')]")
        except:

            return False

        return True

    def wait_is_open_container(self):
        for _try in range(5):
            is_open = self.is_open_container()

            if not is_open:
                time.sleep(1)

                continue

            return True

        return False

    def loop_open_images(self):
        for _try in range(3):

            is_open = self.is_open_container()

            if not is_open:
                res_click = self.open_container_images()

                time.sleep(5)

            loop_full_load_page(self.driver)

            close_popup(self.driver)

            is_open_wait = self.wait_is_open_container()

            if not is_open_wait:
                time.sleep(1)

                continue

            return True

        error_ = f'Закончились попытки получения картинок товара'

        logger_msg(error_)

        return ''

    def get_image_list(self):
        try:
            images_links = self.driver.find_elements(by=By.XPATH, value=f"//*[contains(@class, 'zoomable')]//img")
        except:
            return False

        try:
            images_links = [x.get_attribute('src') for x in images_links]
        except:
            return False

        return images_links

    def loop_get_image_list(self):
        for _try in range(3):
            images_links = self.get_image_list()

            if not images_links:
                time.sleep(1)

                continue

            return images_links

        error_ = f'Закончились попытки получить ссылки на изображения товара'

        logger_msg(error_)

        return False

    def click_next_img(self):
        try:
            self.driver.find_element(by=By.XPATH,
                                     value=f"//*[contains(@class, 'actions')]"
                                           f"//button[contains(@class, 'next')]").click()
        except:
            return False

        return True

    def close_container(self):
        try:
            self.driver.find_element(by=By.XPATH,
                                     value=f"//*[contains(@class, 'toolbar')]"
                                           f"//*[contains(@class, 'close')]").click()
        except:
            return False

        return True

    def loop_get_all_images(self):
        images_links = []

        for _try in range(10):
            images_links = self.loop_get_image_list()

            if images_links and len(images_links) == len(self.images):
                return True

            self.images = images_links

            loop_close_jivo(self.driver)

            for _trys in range(2):
                self.click_next_img()

                loop_full_load_page(self.driver)

                time.sleep(2)

            continue

        error_ = f'Закончились попытки прокликать на все картинки! Проверить'

        logger_msg(error_)

        return images_links

    def get_text_links(self):
        try:
            text_image = ' '.join(link for link in self.images)
        except Exception as es:
            error_ = f'Не могу сформировать текстовый список ссылок изображений товара "{es}"'

            logger_msg(error_)

            return ''

        return text_image

    def loop_close_container(self):
        for _tr in range(3):
            is_open = self.is_open_container()

            if not is_open:
                return True

            res_click = self.close_container()

            time.sleep(1)

            continue

        error_ = f'Кончились попытки закрыть окно с картинками'

        logger_msg(error_)

        return False

    def loop_get_images(self):
        is_open_container = self.loop_open_images()

        if not is_open_container:
            return ''

        image_list = self.loop_get_all_images()

        good_image = self.get_text_links()

        self.loop_close_container()

        return good_image
