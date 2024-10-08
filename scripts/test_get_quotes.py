import os
import requests
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv(dotenv_path="../config/.env")
API_KEY = os.getenv("TRADIER_API_KEY")

# Define the Get Quotes endpoint
quotes_endpoint = "https://api.tradier.com/v1/markets/quotes"

# Set up headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

# Define parameters
params = {
    'symbols': 'AAPL,TSLA,SPY',  # Replace with the symbols you want
    'greeks': 'false'            # Set to 'true' to include options greeks
}

# Make the request to get quotes
response = requests.get(quotes_endpoint, headers=headers, params=params)
json_response = response.json()

# Check the status and print the response
if response.status_code == 200:
    print("Quotes data retrieved successfully.")
    print(json_response)
else:
    print(f"Failed to retrieve quotes data. Status code: {response.status_code}")
    print(json_response)