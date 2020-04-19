import pandas as pd

def transform_data(event, context):
    file = event
    for k in file:
        print(k)