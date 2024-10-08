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


def get_document(driver):
    try:
        documents = driver.find_elements(by=By.XPATH, value=f"//*[@class='docs']//a")
    except:
        return False

    return documents


def formate_documents(documents):
    good_links = []

    for row in documents:
        try:
            link = row.get_attribute('href')
        except:
            continue

        try:
            name = row.find_element(by=By.XPATH, value=f"./span[contains(@class, 'title')]").text
        except:
            name = 'Документ'

        good_value = f'*{name}*{link}'

        good_links.append(good_value)

    return_links = ' '.join(x for x in good_links)

    return return_links


def loop_get_document(driver):
    for _try in range(3):
        document_elem = get_document(driver)

        if not document_elem:
            time.sleep(1)

            continue

        documents = formate_documents(document_elem)

        return documents

    error_ = f'Закончились попытки получения документов товара'

    logger_msg(error_)

    return ''
