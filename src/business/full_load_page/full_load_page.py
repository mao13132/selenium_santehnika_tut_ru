# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from src.logger._logger import logger_msg


def load_full_page(driver):
    try:
        status = driver.execute_script("return document.readyState")
    except Exception as es:
        error = f'Не могу получить статус загрузки страницы "{es}"'

        logger_msg(error)

        return False

    if status == 'complete':
        return True
    else:
        return False


def loop_full_load_page(driver):
    for _try in range(60):

        full_load = load_full_page(driver)

        if not full_load:
            time.sleep(1)

            continue

        return True

    error = f'Закончились все попытки дождаться полной загрузки страницы'

    logger_msg(error)

    return False
