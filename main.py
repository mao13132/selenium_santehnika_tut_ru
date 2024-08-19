# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import sys
import traceback

from settings import MODE_GET_LINKS
from src.browser.createbrowser import CreatBrowser
from src.business.start_business import StartBusiness
from src.logger._logger import logger_msg
from src.sql.bot_connector import BotDB


def main(driver):
    if MODE_GET_LINKS:
        settings_task = {
            'driver': driver,
            'BotDB': BotDB
        }

        res_task = StartBusiness(settings_task).start_business()

    print(f'Работу окончил. Результат: {res_task}')

    return True


if __name__ == '__main__':
    browser = CreatBrowser('santehnika')

    try:
        res = main(browser.driver)
    except Exception as es:

        msg = f'Parser Santehnika Tut ⭕️: ошибка главного потока "{es}"'

        logger_msg(f"{msg}\n"
                   f"{''.join(traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]))}")

    finally:
        try:
            browser.driver.quit()
        except:
            pass
