# test_tradier_api.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="../config/.env")

# Get API key from environment variables
API_KEY = os.getenv("TRADIER_API_KEY")

# Define Tradier API endpoint (example: Get account balance)
endpoint = "https://api.tradier.com/v1/markets/quotes"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}
params = {
    "symbols": "AAPL,TSLA"  # Example symbols to query
}

# Make the API request
response = requests.get(endpoint, headers=headers, params=params)

# Check for success and print the response
if response.status_code == 200:
    print("Success!")
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text)