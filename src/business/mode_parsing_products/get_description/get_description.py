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


def get_description(driver):
    try:
        descriptions = driver.find_element(by=By.XPATH, value=f"//*[contains(@class, 'content') and "
                                                              f"contains(@class, 'tabs')]"
                                                              f"//*[contains(@class, 'tab_des')]").text
    except:
        return False

    return descriptions


def loop_get_description(driver):
    for _try in range(3):
        descriptions = get_description(driver)

        if not descriptions:
            time.sleep(1)

            continue

        return descriptions

    error_ = f'Закончились попытки получения описание товара'

    logger_msg(error_)

    return ''
