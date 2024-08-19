# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from datetime import datetime

from settings import PARSE_URL
from src.business.add_links_from_sql.add_links_from_sql import add_links_from_sql
from src.business.close_popup.close_popup import close_popup
from src.business.get_all_products.get_all_products import loop_get_all_products
from src.business.get_count_page.get_count_page import loop_get_count_page
from src.business.load_page import LoadPage
from src.business.paginator_click.paginator_click import loop_paginator_click


class StartBusiness:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

        self.BotDB = settings['BotDB']

    def start_business(self):

        res_load = LoadPage(self.driver, PARSE_URL).loop_load_page("//*[contains(@class, 'logo')]")

        if not res_load:
            return False

        close_popup(self.driver)

        all_count_page = loop_get_count_page(self.driver)

        for page in range(all_count_page):
            current_page = page + 1

            print(f'{datetime.now().strftime("%H:%M:%S")} Страница {current_page}: Начинаю получение ссылок на товары')

            link_products = loop_get_all_products(self.driver)

            if not link_products:
                continue

            res_add_sql = add_links_from_sql(link_products, self.BotDB)

            next_page = current_page + 1

            if next_page <= all_count_page:
                res_click_paginator = loop_paginator_click(self.driver, next_page)

            print(f'{datetime.now().strftime("%H:%M:%S")} Обработал страницу {current_page}')

        print(f'{datetime.now().strftime("%H:%M:%S")} Закончил обработку всех страницу')

        return True
