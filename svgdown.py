import os
import requests
from wand.image import Image
from wand.api import library
import pandas as pd

os.environ['MAGICK_HOME'] = 'C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI'

library.MagickWandGenesis()

df = pd.read_csv('sorted_dataset copy 2.csv')


for index, row in df.iterrows():
    logo_url = row['Logo URL']
    brand_name = row['Brand Name']

    if isinstance(logo_url, str) and logo_url.strip() != '':
        response = requests.get(logo_url+'?size=200')
        if response.status_code == 200:
            # Process the image
            with Image(blob=response.content) as img:
                filename = f"{brand_name}.svg"
                filepath = os.path.join("downsvgs", filename)
                os.makedirs("downsvgs", exist_ok=True)
                img.format = 'svg'
                img.save(filename=filepath)

            print(f"SVG image '{
                  filename}' downloaded successfully inside the 'downsvgs' folder.")
        else:
            print(f"Failed to download image from {
                  logo_url}. Status code: {response.status_code}")
    else:
        print(f"Skipping NA or empty URL: {logo_url}")
