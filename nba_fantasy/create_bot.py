from aiogram import Dispatcher, Bot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(os.getenv('bot_token'))
dp = Dispatcher(bot)

headers = {'Ocp-Apim-Subscription-Key': os.getenv('api_token')}
