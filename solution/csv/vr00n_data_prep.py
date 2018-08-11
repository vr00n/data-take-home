import sys
import csv
import pandas as pd
from dateutil import parser
import datetime
import re


data = pd.read_csv('../../files/data.csv')
state = pd.read_csv('../../files/state_abbreviations.csv')
data['start_date_description']="na"

for index, row in data.iterrows():
# String cleaning
    data.at[index,'bio'] = re.sub( '\s+', ' ', row['bio'] ).strip()
# Code Swap
    data.at[index,'state'] = state.loc[state['state_abbr'] == row['state']].state_name.to_string().split()[1]
# Date Offset
    if len(row['start_date']) < 8:
        data.at[index,'start_date_description'] = "Invalid Date"
    else:
        try:
            d = parser.parse(row['start_date'])
            data.at[index,'start_date_description'] = d.strftime("%Y-%m-%d")
        except ValueError:
            data.at[index,'start_date_description'] = "Invalid Date"
data.to_csv('enriched.csv')
