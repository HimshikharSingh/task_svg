import os
import requests
from wand.image import Image
from wand.api import library
import pandas as pd

os.environ['MAGICK_HOME'] = 'C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI'

library.MagickWandGenesis()

# Define the URL of the image with query parameters
image_url = "https://logo.clearbit.com/savealot.com?size=200"

# Send a GET request to fetch the image
response = requests.get(image_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the image content to SVG format using wand
    with Image(blob=response.content) as img:
        # Define the filename to save the SVG image
        filename = "savealot_logo.svg"
        # Define the filepath to save the SVG image inside the "downsvgs" folder
        filepath = os.path.join("newfolder", filename)

        img.format = 'svg'
        img.save(filename=filepath)

    print(f"SVG image '{
          filename}' downloaded successfully inside the 'downsvgs' folder.")
else:
    print(f"Failed to download image from {
          image_url}. Status code: {response.status_code}")
