import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:admin@localhost:5433/itransition')

df = pd.read_json('task1_valid.json')


#df['id'] = df['id'].astype('int64')
df['id'] = df['id'].astype(str)


df.to_sql('books', engine, schema = 'task1', if_exists='append', index=False)

print("GOOD")
