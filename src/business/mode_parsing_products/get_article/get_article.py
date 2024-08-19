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


def get_article(driver):
    try:
        article = driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Артикул')]/parent::span"
                                                         f"/parent::li/div").text
    except:
        return False

    return article


def loop_get_article(driver):
    for _try in range(3):
        article = get_article(driver)

        if not article:
            time.sleep(1)

            continue

        return article

    error_ = f'Закончились попытки получения артикула товара'

    logger_msg(error_)

    return ''
