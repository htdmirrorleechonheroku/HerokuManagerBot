import os

class Config:
    BOT_TOKEN = os.environ.get("5213193325:AAEEuiqQO1hrzWaOpv542biBTXApClyt8YI","")
    HEROKU_API_KEY = os.environ.get("dd26273b-f962-4eef-8c23-e3e429af703d","")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("5108941922").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("htdherokumanager","")
