import base64
import requests
from google.cloud import storage
from dotenv import load_dotenv
load_dotenv()
import os

def fetch_data(input):
    data = requests.get(input)
    return data.text

def store_data(data):
    try:
        # Instantiates a client
        storage_client = storage.Client()
        bucket = storage_client.get_bucket("bucket-data_raw")
        bucket_csv = bucket.blob('data_us_nyt.csv')
        bucket_csv.upload_from_string(data)
        print("complete!")
    except Exception as e:
        print(str(e))

def main():
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    data_fetched = fetch_data(url)
    store_data(data_fetched)
