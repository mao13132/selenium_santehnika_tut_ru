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


def get_name(driver):
    try:
        name = driver.find_element(by=By.XPATH,
                                    value=f"//*[@class='container']//*[contains(@class, 'title')]/h1").text
    except:
        return False

    return name


def loop_get_name(driver):
    for _try in range(3):
        name = get_name(driver)

        if not name:
            time.sleep(1)

            continue

        return name

    error_ = f'Закончились попытки получения имени товара'

    logger_msg(error_)

    return ''
