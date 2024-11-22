import sqlite3
import os
from dataclasses import dataclass

class Database:
    def __init__(self):
        self.db_file = os.getenv("DB_FILE")
    def __enter__(self):
        self.__connection = sqlite3.connect(self.db_file)
        return self

    def __exit__(self, type, value, traceback):
        self.__connection.commit()
        self.__connection.close()

    def get_header_links(self):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT link, name FROM my_links;")
        return cursor.fetchall()


