from pymongo import MongoClient
import datetime
import configparser

# load mongo_config files

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mongo_config","hostname")
username = parser.get("mongo_config","username")
password = parser.get("mongo_config","password")
database_name = parser.get("mongo_config","database")
collection_name = parser.get("mongo_config","collection")

mongo_client = MongoClient("mongodb+srv://"+username+":"+password+"@"+hostname+"/"+database_name+"?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

