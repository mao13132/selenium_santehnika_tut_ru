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


def get_products(driver):
    try:
        links = driver.find_elements(by=By.XPATH,
                                     value=f"//*[contains(@id, 'insideCatalog')]"
                                           f"//div[contains(@class, 'p_item')]/a")
    except:
        return False

    return links


def get_links_by_row(rows):
    link_list = []

    for row in rows:
        try:
            link = row.get_attribute('href')
        except Exception as es:
            error_ = f'Ошибка при получение ссылки из строки "{es}"'

            logger_msg(error_)

            continue

        link_list.append(link)

    return link_list


def loop_get_all_products(driver):
    for _try in range(3):
        products_data = get_products(driver)

        if not products_data:
            time.sleep(1)

            continue

        links_list = get_links_by_row(products_data)

        return links_list

    error_ = f'Закончились попытки получить ссылки на товар'

    logger_msg(error_)

    return False
