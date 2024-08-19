# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By


def check_popup(driver):
    try:
        _value = driver.find_element(by=By.XPATH,
                                      value=f"//*[contains(@class, 'popmechanic') and "
                                            f"contains(@class, 'close')]").click()
    except:
        return False

    return True


def close_popup(driver):
    exist_popup = check_popup(driver)

    return exist_popup
