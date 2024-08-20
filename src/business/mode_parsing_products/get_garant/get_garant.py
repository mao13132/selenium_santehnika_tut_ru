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


def get_garant(driver):
    try:
        garant = driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Гарантийный срок')]/parent::span"
                                                        f"/parent::li/div").text
    except:
        return False

    return garant


def loop_get_garant(driver):
    for _try in range(3):
        garant = get_garant(driver)

        if not garant:
            time.sleep(1)

            continue

        return garant

    error_ = f'Закончились попытки получения гарантии товара'

    logger_msg(error_)

    return ''
