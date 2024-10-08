import os
import requests
from dotenv import load_dotenv

# Load the API key and account ID from the .env file
load_dotenv(dotenv_path="../config/.env")
API_KEY = os.getenv("TRADIER_API_KEY")
ACCOUNT_ID = os.getenv("TRADIER_ACCOUNT_ID")

# Define the Gain/Loss endpoint
gain_loss_endpoint = f"https://api.tradier.com/v1/accounts/{ACCOUNT_ID}/gainloss"

# Set up headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

# Define parameters (adjust as needed)
params = {
    'page': '1',
    'limit': '100',
    'sortBy': 'closeDate',
    'sort': 'desc',            # Use 'asc' for ascending order if needed
    'start': '2024-01-01',     # Replace with desired start date
    'end': '2024-12-31',       # Replace with desired end date
    'symbol': ''            # Replace with a specific symbol, or omit for all symbols
}

# Make the request to get gain/loss data
response = requests.get(gain_loss_endpoint, headers=headers, params=params)
json_response = response.json()

# Check the status and print the response
if response.status_code == 200:
    print("Gain/Loss data retrieved successfully.")
    print(json_response)
else:
    print(f"Failed to retrieve gain/loss data. Status code: {response.status_code}")
    print(json_response)