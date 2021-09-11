

from bs4 import BeautifulSoup
import requests
import boto3
from datetime import datetime
import json


def lambda_handler(event, context):

    s3 = boto3.resource('s3')
    r  = requests.get("https://download.bls.gov/pub/time.series/pr/")
    data = r.text
    soup = BeautifulSoup(data,features="html.parser")

    for link in soup.find_all('a'):
        #print(link.get('href'))
        full_url="https://download.bls.gov"+link.get('href')
        #print(full_url)
        r=requests.get(full_url)
        raw_request = (r.text)
        #print(raw_request)
        data = raw_request
        s3_path = link.get('href')
        s3.Object('kkudylambdazips', s3_path).put(Body=data)
    print("timeseries upload complete")
    url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
    r = requests.get(url)
    files = json.loads(r.text)
    user_encode_data = json.dumps(files, indent=2).encode('utf-8')
    s3.Object('kkudylambdazips', "usdata.json").put(Body=user_encode_data)

    print("population data upload complete")
