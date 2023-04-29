from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

DB_PASS = os.getenv('DB_PWD')
DB_USERNAME = os.getenv('DB_USERNAME')

# Connect to MongoDB Atlas with credentials
client = MongoClient(f"mongodb+srv://{DB_USERNAME}:{DB_PASS}@cluster1.bztqi43.mongodb.net/avs_db?retryWrites=true&w=majority")
db = client['avs_db']

collection = db['addresses']
api_key_collection = db['api_keys']

# create text index for search
collection.create_index([('addressLine1', 'text')])

# Defines schema for the addresses in the database
address_schema = {
  'addressLine1': str,
  'addressLine2': str,
  'city': str,
  'stateProv': str,
  'postalCode': str,
  'country': str,
}

api_key_schema = {
  'api_key': str,
  'client_ip': str,
  'created': str
}