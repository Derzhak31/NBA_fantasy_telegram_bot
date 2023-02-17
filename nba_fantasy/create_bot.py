from aiogram import Dispatcher, Bot
import os
import psycopg2
import requests
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(os.getenv('bot_token'))
dp = Dispatcher(bot)

user = 'postgres'
password = os.getenv('pass_db')
db_name = 'NBA_fantasy'


class DB:

    def __init__(self):
        self.conn = psycopg2.connect(user=user, password=password, database=db_name)

    def cur(self):
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        return self.cursor

    def close(self):
        self.closed = self.conn.close()
        return self.closed


class API:
    headers = {'Ocp-Apim-Subscription-Key': os.getenv('api_token')}

    def __init__(self, url: str):
        self.response = requests.get(url, headers=self.headers).text

    def data(self):
        self.data = json.loads(self.response)
        return self.data
