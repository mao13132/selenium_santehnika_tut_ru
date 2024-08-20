# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from datetime import datetime

from src.business.close_popup.close_popup import close_popup
from src.business.load_page import LoadPage
from src.business.mode_parsing_products.get_all_specifications.get_all_specifications import loop_get_all_specifications
from src.business.mode_parsing_products.get_article.get_article import loop_get_article
from src.business.mode_parsing_products.get_brand.get_brand import loop_get_brand
from src.business.mode_parsing_products.get_category.get_category import loop_get_category
from src.business.mode_parsing_products.get_color.get_color import loop_get_color
from src.business.mode_parsing_products.get_country.get_country import loop_get_country
from src.business.mode_parsing_products.get_description.get_description import loop_get_description
from src.business.mode_parsing_products.get_document.get_document import loop_get_document
from src.business.mode_parsing_products.get_garant.get_garant import loop_get_garant
from src.business.mode_parsing_products.get_images.get_images import GetImage
from src.business.mode_parsing_products.get_name.get_name import loop_get_name
from src.business.mode_parsing_products.get_price.get_price import loop_get_price
from src.business.mode_parsing_products.go_specifications.go_specifications import go_specifications


class StartParsingProducts:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

        self.BotDB = settings['BotDB']

    def start_parsing_products(self):
        products_list = self.BotDB.get_all_links()

        if not products_list:
            return False

        print(f'{datetime.now().strftime("%H:%M:%S")} Начинаю обработку "{len(products_list)}" товаров')

        for count, sql_row in enumerate(products_list):
            id_link = sql_row[0]

            link = sql_row[1]

            print(f'{datetime.now().strftime("%H:%M:%S")} {count + 1} Начинаю обработку "{link}"')

            res_load = LoadPage(self.driver, link).loop_load_page("//*[contains(@class, 'logo')]")

            if not res_load:
                continue

            close_popup(self.driver)

            name = loop_get_name(self.driver)

            price = loop_get_price(self.driver)

            brand = loop_get_brand(self.driver)

            article = loop_get_article(self.driver)

            country = loop_get_country(self.driver)

            color = loop_get_color(self.driver)

            description = loop_get_description(self.driver)

            images = GetImage(self.driver).loop_get_images()

            res_go = go_specifications(self.driver)

            category = loop_get_category(self.driver)

            garant = loop_get_garant(self.driver)

            specifications = loop_get_all_specifications(self.driver)

            documents = loop_get_document(self.driver)

            products = {
                'link': link,
                'name': name,
                'price': price,
                'brand': brand,
                'article': article,
                'country': country,
                'color': color,
                'description': description,
                'images': images,
                'res_go': res_go,
                'category': category,
                'specifications': specifications,
                'documents': documents,
                'garant': garant,
            }

            res_add = self.BotDB.add_products(products)

            if res_add:
                self.BotDB.disable_link(id_link)

            print(f'{datetime.now().strftime("%H:%M:%S")} Обработал {count + 1}')

        print(f'{datetime.now().strftime("%H:%M:%S")} Закончил обработку всех товаров')
