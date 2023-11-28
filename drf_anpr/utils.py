import csv 
import os 
import pandas as pd

class InputData:
    def __init__(self):
        self.basepath = os.path.dirname(os.path.abspath(__file__))
        self.source = os.path.join(self.basepath, "data", "member_registry.csv")
            
    def read_csv(self):
        # with open(self.source, 'r') as doc:
        #     csvread = csv.DictReader(doc, delimiter=',')
        #     for row in csvread:
                # print(row)
        df = pd.read_csv(self.source)
        df_new = df[['name']]
        print(df_new)

if __name__ == "__main__":
    InputData().read_csv()
