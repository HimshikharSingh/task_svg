import requests
import pandas as pd
import time

api_key = 'sk_c8bbc1fbd9f228f0f4c6aa573536f785'

df = pd.read_csv('sorted_dataset copy 2.csv')

# Create new columns for Domain and Logo URL
df['Domain'] = ''
df['Logo URL'] = ''

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Extract the company name from the 'Brand Name' column
    name = row['Brand Name']

    # Define the API endpoint
    url = f'https://company.clearbit.com/v1/domains/find?name={name}'

    # Set the request headers with your API key
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the domain and logo URL from the response
        domain = data.get('domain')
        logo_url = data.get('logo')

        # Update the DataFrame with the domain and logo URL
        df.loc[index, 'Domain'] = domain
        df.loc[index, 'Logo URL'] = logo_url

        print(f"Company Name: {name}")
        print(f"Domain: {domain}")
        print(f"Logo URL: {logo_url}")
    else:
        # If the request was not successful, set 'NA' in the DataFrame
        df.loc[index, 'Domain'] = 'NA'
        df.loc[index, 'Logo URL'] = 'NA'
        print(f"Error: {response.status_code} - {response.text}")

    # Add a delay of 5 seconds before making the next API call
    time.sleep(5)

# Save the updated DataFrame to a new CSV file
df.to_csv('sorted_dataset copy 2.csv', index=False)
print(df.head())
