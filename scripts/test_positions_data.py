import os
import requests
from dotenv import load_dotenv

# Load the API key and account ID from the .env file
load_dotenv(dotenv_path="../config/.env")
API_KEY = os.getenv("TRADIER_API_KEY")
ACCOUNT_ID = os.getenv("TRADIER_ACCOUNT_ID")

# Define the Positions endpoint
positions_endpoint = f"https://api.tradier.com/v1/accounts/{ACCOUNT_ID}/positions"

# Set up headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

# Make the request to get account positions
response = requests.get(positions_endpoint, headers=headers)
json_response = response.json()

# Check the status and print the response
if response.status_code == 200:
    print("Positions data retrieved successfully.")
    print(json_response)
else:
    print(f"Failed to retrieve positions data. Status code: {response.status_code}")
    print(json_response)