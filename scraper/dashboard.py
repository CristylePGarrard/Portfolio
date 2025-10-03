import os
import pandas as pd
import time
from dash import dcc


# LOCATE FILES
files = os.listdir()
all_files = [x for x in files if str(x).startswith('all_data_')]
# CHECK AT LEAST ONE FILE IN ARRAY
assert len(all_files) > 0

file_dates = {}

for val in all_files:
    filename = str(val)
    filedate = os.path.getmtime(val)
    file_dates[filename] = filedate

use_file = max(zip(file_dates.values(), file_dates.keys()))[1]

df = pd.read_csv(use_file)

df['filetime'] = df['filetime'].astype(str)
df.loc[df['filetime'] == '0', 'filetime'] = '0000'
df['dt'] = df['filedate'] + '-' + df['filetime']
df['dt'] = pd.to_datetime(df['dt'], format='%m-%d-%Y-%H%M')

df = df.loc[df['Strain Type'].notna()]
df.reset_index(inplace=True, drop=True)

# CHART TO SHOW COUNT OF PRODUCT BY STRAIN PER DAY
# list of fliedates
# list of strain types
# list of counts 
data_dict = {}
for g in df.groupby('dt'):
    strains = g[1].groupby('Strain Type').count()['filename'].index.tolist()
    counts = g[1].groupby('Strain Type').count()['filename'].values.tolist()
    data_dict[g[0]] = [strains, counts]


data = []
for k in data_dict.keys()
    temp = {}
    temp['type'] = 'bar'
    temp['name'] = str(k)
    temp['x'] = list(data_dict.get(k))[0]
    temp['y'] = list(data_dict.get(k))[1]
    data.append(temp)




# SAVE FILE
from datetime import datetime
savefile = 'all_data' + datetime.now().strftime('_%m_%d_%Y_%H%M') + '.txt'
with open(savefile, 'w') as f:
    all_data.to_csv(f, index=False)

