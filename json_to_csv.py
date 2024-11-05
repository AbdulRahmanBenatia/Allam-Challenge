import pandas as pd

df = pd.read_json('train.json')

df.to_csv('train.csv', index=False, encoding='utf-8')
