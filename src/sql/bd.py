import datetime
import sqlite3
from datetime import datetime

from src.logger._logger import logger_msg


class BotDB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, db_file):
        try:

            self.conn = sqlite3.connect(db_file, timeout=30)
            print('Подключился к SQL DB:', db_file)
            self.cursor = self.conn.cursor()
            self.check_table()
        except Exception as es:
            print(f'Ошибка при работе с SQL {es}')

    def check_table(self):

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                                f"links (id_pk INTEGER PRIMARY KEY AUTOINCREMENT, "
                                f"link TEXT, pars BOOLEAN DEFAULT 0, other TEXT)")

        except Exception as es:
            print(f'SQL исключение check_table links {es}')

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                                f"products (id_pk INTEGER PRIMARY KEY AUTOINCREMENT, "
                                f"link TEXT, "
                                f"name TEXT, "
                                f"price NUMERIC, "
                                f"brand TEXT, "
                                f"article TEXT, "
                                f"country TEXT, "
                                f"color TEXT, "
                                f"description TEXT, "
                                f"images TEXT, "
                                f"category TEXT, "
                                f"specifications TEXT, "
                                f"documents TEXT, "
                                f"garant TEXT, "
                                f"other TEXT)")

        except Exception as es:
            print(f'SQL исключение check_table products {es}')

    def get_all_links(self):
        try:
            result = self.cursor.execute(f"SELECT * FROM links WHERE pars='0'")

            response = result.fetchall()
        except Exception as es:
            logger_msg(f'SQL ошибка get_all_links "{es}" ')

            return False

        return response

    def get_all_products(self):
        try:
            result = self.cursor.execute(f"SELECT * FROM products")

            response = result.fetchall()
        except Exception as es:
            logger_msg(f'SQL ошибка get_all_products "{es}" ')

            return False

        return response

    def exist_link(self, link):
        result = self.cursor.execute(f"SELECT * FROM links "
                                     f"WHERE link='{link}'")

        response = result.fetchall()

        if response == []:
            return False

        return True

    def add_link(self, link):
        result = self.cursor.execute(f"SELECT * FROM links WHERE link='{link}'")

        response = result.fetchall()

        if not response:
            self.cursor.execute("INSERT OR IGNORE INTO links ('link') VALUES (?)",
                                (link,))

            self.conn.commit()

            return True

        return False

    def add_products(self, products):
        result = self.cursor.execute(f"SELECT * FROM products WHERE link='{products['link']}'")

        response = result.fetchall()

        if not response:
            import json

            try:

                specifications = json.dumps(products['specifications'])

                self.cursor.execute("INSERT OR IGNORE INTO products ('link', 'name', 'price', 'brand', 'article', "
                                    "'country', 'color', 'description', 'images', 'category', 'specifications', "
                                    "'documents', 'garant') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                    (products['link'], products['name'], products['price'], products['brand'],
                                     products['article'], products['country'], products['color'],
                                     products['description'],
                                     products['images'], products['category'], specifications,
                                     products['documents'], products['garant']))

                self.conn.commit()

            except Exception as es:
                error_ = f'SQL ошибка add_products: "{es}"'

                logger_msg(error_)

                return False

            return True

        return False

    def disable_link(self, id_pk):

        try:

            self.cursor.execute(f"UPDATE links SET pars = 1 WHERE id_pk = '{id_pk}'")

            self.conn.commit()

        except Exception as es:

            print(f'SQL Ошибка при disable_link "{es}"')

            return False

        return True

    def close(self):
        # Закрытие соединения
        self.conn.close()

        print('Отключился от SQL BD')
