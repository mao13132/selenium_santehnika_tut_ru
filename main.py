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

from settings import MODE_GET_LINKS, MODE_PARSING_PRODUCTS
from src.browser.createbrowser import CreatBrowser
from src.business.mode_get_links.start_get_links import StartGetLinks
from src.business.mode_parsing_products.start_parsing_products import StartParsingProducts
from src.logger._logger import logger_msg
from src.sql.bot_connector import BotDB


def main(driver):
    if MODE_GET_LINKS:
        print(f'Запущен режим сбора ссылок на товар')

        settings_task = {
            'driver': driver,
            'BotDB': BotDB
        }

        res_task = StartGetLinks(settings_task).start_get_links()

    if MODE_PARSING_PRODUCTS:

        settings_parsing = {
            'driver': driver,
            'BotDB': BotDB
        }

        res_parsing = StartParsingProducts(settings_parsing).start_parsing_products()

    print(f'Закончил работу программы')

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
