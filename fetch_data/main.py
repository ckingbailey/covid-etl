import base64
import requests
from google.cloud import storage
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import *

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
gcp_project = "test-python-etl"
service_account = "service-account_local-dev"

def fetch_data(input):
    data = requests.get(input)
    #text = data.text
    text = data.text[0:1000]
    print(text)

def store_data():
    # Instantiates a client
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("bucket-data_raw")
    bucket_csv = bucket.blob('data_us_nyt.csv')
    bucket_csv.upload_from_string("placeholder")
    print("complete!")

# # Then do other things...
# blob = bucket.get_blob('remote/path/to/file.txt')
# print(blob.download_as_string())
# blob.upload_from_string('New contents!')
# blob2 = bucket.blob('remote/path/storage.txt')
# blob2.upload_from_filename(filename='/local/path.txt')

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print("Message: " + pubsub_message)


print("start at: " + str(datetime.now()))
store_data()