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


def move_to_specifications(driver):
    try:
        element = driver.find_element(by=By.XPATH, value=f"//*[@class='tabs_content']")
    except:
        return False

    try:
        ActionChains(driver).move_to_element(element).perform()
    except:
        return False

    return True


def click_by_specifications(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(text(), 'арактеристики')]").click()
    except:
        return False

    return True


def check_status_active(driver):
    try:
        status = driver.find_element(by=By.XPATH,
                                     value=f"//a[contains(text(), 'арактеристики')]").get_attribute('class')
    except:
        return False

    if 'active' in status:
        return True

    return False


def loop_go_specifications(driver):
    for _try in range(3):
        is_active = check_status_active(driver)

        if is_active:
            return True

        res_click = click_by_specifications(driver)

        time.sleep(1)

        loop_full_load_page(driver)

        continue

    error_ = f'Кончились попытки перейти в характеристики'

    logger_msg(error_)

    return False


def go_specifications(driver):
    move_to_specifications(driver)

    loop_full_load_page(driver)

    res_go = loop_go_specifications(driver)

    return res_go
