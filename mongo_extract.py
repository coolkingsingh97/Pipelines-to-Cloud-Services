from pymongo import MongoClient
import csv
import boto3
import datetime
from datetime import timedelta
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

mongo_db = mongo_client[database_name]
mongo_collection = mongo_db[collection_name]

start_date = datetime.datetime.today() + timedelta(days=-1)
end_date = start_date + timedelta(days=1)

mongo_query = {"$and":[{"event_timestamp":{"$gte":start_date}},{"event_timestamp":{"$lt":end_date}}]}

event_docs = mongo_collection.find(mongo_query,batch_size=3000)

# create a blank list to store the results

all_events = []

# iterate through the cursor

for doc in event_docs:
    # Include default values
    event_id = str(doc.get("event_id",-1))
    event_timestamp = doc.get("event_timestamp",None)
    event_name = doc.get("event_name", None)

    current_event = []
    current_event.append(event_id)
    current_event.append(event_timestamp)
    current_event.append(event_name)

    # add the event to the final list of events
    all_events.append(current_event)

export_file = "export_file.csv"

with open(export_file,'w') as fp:
    csvw = csv.writer(fp,delimiter='|')
    csvw.writerows(all_events)
fp.close()

