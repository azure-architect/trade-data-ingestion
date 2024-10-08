import os
import requests
from dotenv import load_dotenv

# Load environment variables from a custom .env file path
load_dotenv(dotenv_path="../config/.env")

# Load API key and account ID from the .env file
API_KEY = os.getenv("TRADIER_API_KEY")
ACCOUNT_ID = os.getenv("TRADIER_ACCOUNT_ID")

# Define the endpoint
endpoint = f"https://api.tradier.com/v1/markets/options/strikes"

# Set up headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

# Define parameters for the options strikes request
params = {
    'symbol': 'VXX',                  # Symbol for the option chain
    'expiration': '2024-10-11',       # Desired expiration date
    'includeAllRoots': 'true'         # Include all option roots
}

# Make the request to get the options strikes data
response = requests.get(endpoint, headers=headers, params=params)

# Print the JSON response, formatted for easy documentation
if response.status_code == 200:
    print("Options strikes data retrieved successfully.")
    print(response.json())  # This will print the raw JSON response
else:
    print(f"Failed to retrieve options strikes data. Status code: {response.status_code}")
    print(response.json())