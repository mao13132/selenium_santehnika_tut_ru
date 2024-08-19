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

from src.business.utils.clear_value import clear_value
from src.logger._logger import logger_msg


def get_price(driver):
    try:
        price = driver.find_element(by=By.XPATH, value=f"//*[@class='price' and @id='price']").text
    except:
        return False

    return price


def loop_get_price(driver):
    for _try in range(3):
        price = get_price(driver)

        if not price:
            time.sleep(1)

            continue

        price = clear_value(price)

        return price

    error_ = f'Закончились попытки получения стоимости товара'

    logger_msg(error_)

    return ''
