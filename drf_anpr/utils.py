import csv 
import os 
import pandas as pd

class InputData:
    def __init__(self):
        self.basepath = os.path.dirname(os.path.abspath(__file__))
        self.source = os.path.join(self.basepath, "data", "member_registry.csv")
            
    def read_csv(self):

        df = pd.read_csv(self.source)
        df_new = df[['plate_number', 'vehicle_color', 'vehicle_name', 'tenant_name']]
        data_list = df_new.to_dict(orient='records')
        return data_list

