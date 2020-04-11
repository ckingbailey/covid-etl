import base64
import requests

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

def fetch_data(input):
    data = requests.get(input)
    #text = data.text
    text = data.text[0:1000]
    print(text)

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print("Message: " + pubsub_message)

fetch_data(url)