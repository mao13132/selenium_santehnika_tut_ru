# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By

from src.business.close_popup.close_popup import close_popup
from src.business.load_page import LoadPage
from src.business.mode_parsing_products.get_article.get_article import loop_get_article
from src.business.mode_parsing_products.get_brand.get_brand import loop_get_brand
from src.business.mode_parsing_products.get_category.get_category import loop_get_category
from src.business.mode_parsing_products.get_country.get_color import loop_get_country, loop_get_color
from src.business.mode_parsing_products.get_name.get_name import loop_get_name
from src.business.mode_parsing_products.get_price.get_price import loop_get_price


class StartParsingProducts:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

        self.BotDB = settings['BotDB']

    def start_parsing_products(self):
        products_list = self.BotDB.get_all_links()

        if not products_list:
            return False

        for sql_row in products_list:
            id_link = sql_row[0]

            link = sql_row[1]

            res_load = LoadPage(self.driver, link).loop_load_page("//*[contains(@class, 'logo')]")

            if not res_load:
                continue

            close_popup(self.driver)

            name = loop_get_name(self.driver)

            category = loop_get_category(self.driver)

            price = loop_get_price(self.driver)

            brand = loop_get_brand(self.driver)

            article = loop_get_article(self.driver)

            country = loop_get_country(self.driver)

            color = loop_get_color(self.driver)

            print()

        print()