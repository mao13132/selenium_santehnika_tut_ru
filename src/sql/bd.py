import datetime
import sqlite3
from datetime import datetime


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
            print(f'SQL исключение check_table monitoring {es}')

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

    def close(self):
        # Закрытие соединения
        self.conn.close()

        print('Отключился от SQL BD')
