# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By

from src.business.mode_get_links.full_load_page.full_load_page import loop_full_load_page


def close_jivo(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(@id, 'jivo_close_button')]").click()
    except:
        return False

    return True


def loop_close_jivo(driver):
    for _try in range(5):
        res_click = close_jivo(driver)

        loop_full_load_page(driver)

    return True
