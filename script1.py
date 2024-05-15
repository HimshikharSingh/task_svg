from bs4 import BeautifulSoup
import requests
import pandas as pd
from searchAPI import search, auth

df = pd.read_csv('sorted_dataset.csv')

# links = {}
df['Brand Urls'] = ""


i = 0
j = 100

urls = {}
coun = 0
for name in list(df['Brand Name'][i:j]):
    v = search(auth(name))
    urls.update(v)
    coun += 1


print(urls)
print(coun)
