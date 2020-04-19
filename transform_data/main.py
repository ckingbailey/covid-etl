import pandas as pd
import datetime

def file_to_dataframe(filepath):
    with open(filepath, 'r') as file_contents:
        frame = pd.read_csv(file_contents, dtype={
            'fips': 'category'
        })
        frame['date'] = pd.to_datetime(frame['date'])
        return frame

def transform_frame_data(frame):
    county_cases_by_date = frame.pivot(index='date', columns='county', values='cases')
    print(county_cases_by_date.head())

def enumerate_obj_methods(storage_obj, context):
    for prop in (method_name for method_name in storage_obj if callable(getattr(storage_obj, method_name))):
        print(prop)
        
