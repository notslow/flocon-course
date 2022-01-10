import sys
import pandas as pd


filename = sys.argv[1]

df = pd.read_csv(filename)
df.to_parquet(filename.replace('csv', 'parquet'))