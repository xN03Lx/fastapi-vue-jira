import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()


DB_CLIENT = MongoClient(
    host=os.getenv("MONGO_HOST"),
    port=27017,
    username=os.getenv("MONGO_USERNAME"),
    password=os.getenv("MONGO_PASSWORD")
)


DB = DB_CLIENT[os.getenv("MONGO_DB")]

def close_db_client():
    DB_CLIENT.close()
