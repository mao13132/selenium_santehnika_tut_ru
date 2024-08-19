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


def get_category(driver):
    try:
        category = driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Цвет')]/parent::span"
                                                       f"/parent::li/div").text
    except:
        return False

    return category


def loop_get_category(driver):
    for _try in range(3):
        category = get_category(driver)

        if not category:
            time.sleep(1)

            continue

        return category

    error_ = f'Закончились попытки получения категории товара'

    logger_msg(error_)

    return ''
