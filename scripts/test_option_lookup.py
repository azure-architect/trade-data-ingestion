import os
import requests
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv(dotenv_path="../config/.env")
API_KEY = os.getenv("TRADIER_API_KEY")

# Define the Options Lookup endpoint
options_lookup_endpoint = "https://api.tradier.com/v1/markets/options/lookup"

# Set up headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

# Define parameters
params = {
    'underlying': 'SPY'  # Replace with the underlying symbol you want to look up
}

# Make the request to lookup options
response = requests.get(options_lookup_endpoint, headers=headers, params=params)
json_response = response.json()

# Check the status and print the response
if response.status_code == 200:
    print("Options lookup data retrieved successfully.")
    print(json_response)
else:
    print(f"Failed to retrieve options lookup data. Status code: {response.status_code}")
    print(json_response)