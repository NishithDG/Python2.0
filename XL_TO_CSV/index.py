import pandas as pd
import os
import glob


filepath = str("Sample_Data - Python Assignment.xlsx")
data = pd.read_excel(filepath,sheet_name=None)


for sheet_name,df in data.items():
    df.to_csv('{}.csv'.format(sheet_name))