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


def get_country(driver):
    try:
        country = driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Страна бренда')]/parent::span"
                                                         f"/parent::li/div").text
    except:
        return False

    return country


def loop_get_country(driver):
    for _try in range(3):
        country = get_country(driver)

        if not country:
            time.sleep(1)

            continue

        return country

    error_ = f'Закончились попытки получения страны товара'

    logger_msg(error_)

    return ''
