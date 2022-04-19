import requests
import json
import configparser
import boto3
import csv

lat = 42.36
lon = 71.05

lat_log_params = {"lat":lat,"lon":lon}

api_response = requests.get(
    "http://api.open-notify.org/iss-pass.json",params=lat_log_params
)

response_json = json.loads(api_response.content)

all_passes = []

for response in response_json['response']:
    current_pass = []
    
    #store the lat/long from the request
    current_pass.append(lat)
    current_pass.append(lon)

    # store the duration and risetime of the pass
    current_pass.append(response['duration'])
    current_pass.append(response['risetime'])

    all_passes.append(current_pass)

    export_file = "api_export_file.csv"

    with open(export_file,'w') as fp:
        csvw =csv.writer(fp, delimiter = '|')
        csvw.writerows(all_passes)
    
    fp.close()

