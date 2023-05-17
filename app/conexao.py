from pymongo import MongoClient
import os
from dotenv import load_dotenv

host = os.getenv('MONGO_HOST')
port = int(os.getenv('MONGO_PORT'))
db_name = os.getenv('MONGO_DB')

client = MongoClient(host, port)
db = client[db_name]
