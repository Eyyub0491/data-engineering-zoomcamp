import sys 
import pandas as pd

print('arguments', sys.argv)

month = int(sys.argv[1])



df = pd.DataFrame({"day": [1, 2], "number_of_pass": [3, 4]})
df['month']=month
print(df.head())
df.to_parquet(f'output_{month}.parquet', index=False)


print(f'hello pipeline, month={month}')
