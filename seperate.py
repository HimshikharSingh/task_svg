import pandas as pd

df = pd.read_csv('sorted_dataset copy 2.csv')

nacount = df['Domain'].isna().sum()


print(nacount)
