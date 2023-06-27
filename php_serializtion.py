import pandas as pd
import phpserialize
from collections import OrderedDict
from phpserialize import *
import base64

df = pd.read_csv('data/php-sample-1.csv')

serialized_column = 'shipping_params' 
extracted_columns = {}

def php_deserialize(data):
    return loads(str(data).encode(), charset='gb18030')

data = df['shipping_params'].dropna().apply(php_deserialize)
dfs=[]
for i in data.items():
    dfs.append(pd.DataFrame(i[1],index=[i[0]]))
deserialized = pd.concat(dfs)
final_data = pd.merge(df, deserialized, left_index=True, right_index=True)

print(final_data)