import os
import requests
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv(dotenv_path="../config/.env")
API_KEY = os.getenv("TRADIER_API_KEY")

# Define the Market History endpoint
history_endpoint = "https://api.tradier.com/v1/markets/history"

# Set up headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

# Define parameters
params = {
    'symbol': 'AAPL',              # Replace with the symbol you want
    'interval': 'daily',           # Options: 'daily', 'weekly', 'monthly'
    'start': '2024-05-04',         # Replace with the start date
    'end': '2024-05-05',           # Replace with the end date
    'session_filter': 'all'        # Options: 'all', 'open', 'close', etc.
}

# Make the request to get market history
response = requests.get(history_endpoint, headers=headers, params=params)
json_response = response.json()

# Check the status and print the response
if response.status_code == 200:
    print("Market history data retrieved successfully.")
    print(json_response)
else:
    print(f"Failed to retrieve market history data. Status code: {response.status_code}")
    print(json_response)