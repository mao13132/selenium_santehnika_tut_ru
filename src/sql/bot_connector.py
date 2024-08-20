import os

from settings import patch_project
from src.sql.bd import BotDB
BotDB = BotDB(f"{patch_project}{os.sep}parser.db")

