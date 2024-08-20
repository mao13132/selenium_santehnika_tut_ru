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


def get_color(driver):
    try:
        color = driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Цвет')]/parent::span"
                                                       f"/parent::li/div").text
    except:
        return False

    return color


def loop_get_color(driver):
    for _try in range(3):
        color = get_color(driver)

        if not color:
            time.sleep(1)

            continue

        return color

    error_ = f'Закончились попытки получения цвет товара'

    logger_msg(error_)

    return ''
