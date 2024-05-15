import pandas as pd
import os

df = pd.read_csv('brands_without_SVG_ copy.csv')

df['Brand Logo'] = df['Brand Logo'].apply(
    lambda x: os.path.basename(x.strip()))


def custom_sort_key(file_name):
    extensions_order = {'.jpeg': 0, '.jpg': 1, '.png': 2, '.webp': 3}
    file_extension = os.path.splitext(file_name)[1]
    return extensions_order.get(file_extension.lower(), 4)


df_sorted = df.sort_values(
    by='Brand Logo', key=lambda x: x.map(custom_sort_key))

df_sorted.to_csv('sorted_dataset.csv', index=False)
