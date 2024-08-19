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

from src.logger._logger import logger_msg


def get_brand(driver):
    try:
        brand = driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Производитель')]/parent::span"
                                                       f"/parent::li/div").text
    except:
        return False

    return brand


def loop_get_brand(driver):
    for _try in range(3):
        brand = get_brand(driver)

        if not brand:
            time.sleep(1)

            continue

        return brand

    error_ = f'Закончились попытки получения производителя (brand) товара'

    logger_msg(error_)

    return ''
