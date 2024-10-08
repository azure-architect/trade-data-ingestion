import os
import requests
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv(dotenv_path="../config/.env")
API_KEY = os.getenv("TRADIER_API_KEY")

# Define the Option Chains endpoint
option_chains_endpoint = "https://api.tradier.com/v1/markets/options/chains"

# Set up headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

# Define parameters for the options chain request
params = {
    'symbol': 'VXX',          # Replace with desired symbol
    'expiration': '2024-10-11',  # Replace with desired expiration date (yyyy-mm-dd)
    'greeks': 'true'             # Set to 'true' to include greeks, 'false' otherwise
}

# Make the request to get the option chain
response = requests.get(option_chains_endpoint, headers=headers, params=params)
json_response = response.json()

# Check the status and print the response
if response.status_code == 200:
    print("Option Chains data retrieved successfully.")
    print(json_response)
else:
    print(f"Failed to retrieve Option Chains data. Status code: {response.status_code}")
    print(json_response)