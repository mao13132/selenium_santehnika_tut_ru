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


def get_all_specifications(driver):
    try:
        specifications = driver.find_elements(by=By.XPATH, value=f"//ul[@class='chars']/li")
    except:
        return False

    return specifications


def formate_specifications(elements_list):
    good_specifications = []

    for elem in elements_list:
        try:
            row = elem.text

            row = row.split('\n')

        except:
            continue

        iter_dict = {
            'name': row[0],
            'value': row[1],
        }

        good_specifications.append(iter_dict)

    return good_specifications


def loop_get_all_specifications(driver):
    for _try in range(3):
        specifications = get_all_specifications(driver)

        if not specifications:
            time.sleep(1)

            continue

        list_specifications = formate_specifications(specifications)

        if not list_specifications:
            time.sleep(1)

            continue

        return list_specifications

    error_ = f'Кончились попытки получить все характеристики товара'

    logger_msg(error_)

    return False
