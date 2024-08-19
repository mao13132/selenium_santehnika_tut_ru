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

from src.business.close_popup.close_popup import close_popup
from src.business.mode_get_links.full_load_page.full_load_page import loop_full_load_page
from src.business.mode_get_links.get_count_page.get_count_page import move_to_paginator
from src.logger._logger import logger_msg


def paginator_click(driver, count_page):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(@data-page, '{count_page}')]").click()
    except:
        return False

    return True


def get_current_page(driver):
    try:
        current_page = driver.find_element(by=By.XPATH,
                                           value=f"//*[@class='pag_wrapper']//*[contains(@class, 'pagination')]"
                                                 f"//*[contains(@class, 'active')]").text

        current_page = int(current_page)
    except:
        return False

    return current_page


def loop_paginator_click(driver, count_page):
    for _try in range(5):

        move_to_paginator(driver)

        current_page = get_current_page(driver)

        if count_page == current_page:
            return True

        res_click = paginator_click(driver, count_page)

        if not res_click:
            time.sleep(1)

            continue

        loop_full_load_page(driver)

        close_popup(driver)

        current_page = get_current_page(driver)

        if not current_page:
            time.sleep(1)

            continue

        if count_page != current_page:
            time.sleep(1)

            continue

        return True

    error_ = f'Кончились попытки переключить на {count_page} страницу'

    logger_msg(error_)

    return False
