import os
import requests
from dotenv import load_dotenv

# Load the API key and account ID from the .env file
load_dotenv(dotenv_path="../config/.env")
API_KEY = os.getenv("TRADIER_API_KEY")
ACCOUNT_ID = os.getenv("TRADIER_ACCOUNT_ID")

# Define the History endpoint
history_endpoint = f"https://api.tradier.com/v1/accounts/{ACCOUNT_ID}/history"

# Set up headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

# Define parameters (adjust as needed)
params = {
    'page': '1',
    'limit': '100',  # Max number of records per page
    'type': 'trade, option, ach, wire, dividend, fee, tax, journal, check, transfer, adjustment, interest',
    'start': '2024-01-01',  # Replace with the desired start date
    'end': '2024-12-31',    # Replace with the desired end date
    'symbol': '',        # Filter by symbol, if desired
    'exactMatch': 'true'
}

# Make the request to get account history
response = requests.get(history_endpoint, headers=headers, params=params)
json_response = response.json()

# Check the status and print the response
if response.status_code == 200:
    print("History data retrieved successfully.")
    print(json_response)
else:
    print(f"Failed to retrieve history data. Status code: {response.status_code}")
    print(json_response)