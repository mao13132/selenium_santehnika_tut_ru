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
from selenium.webdriver.common.action_chains import ActionChains

from src.business.mode_get_links.full_load_page.full_load_page import loop_full_load_page
from src.logger._logger import logger_msg


def get_count_page(driver):
    try:
        count_page = driver.find_element(by=By.XPATH,
                                         value=f"//*[@class='pagination']").text

        count_page = int(count_page)

    except:
        return False

    return count_page


def move_to_paginator(driver):
    try:
        paginator_element = driver.find_element(by=By.XPATH,
                                                value=f"//*[@id='brands']")
    except:
        return False

    try:
        ActionChains(driver).move_to_element(paginator_element).perform()
    except:
        return False

    return True


def loop_get_count_page(driver):
    for _try in range(3):
        move_to_paginator(driver)

        loop_full_load_page(driver)

        count_pages = get_count_page(driver)

        if not count_pages:
            time.sleep(1)

            continue

        return count_pages

    error_ = f'Кончились попытки получить кол-во страниц'

    logger_msg(error_)

    return 1
