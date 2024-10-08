import os
import requests
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv(dotenv_path="../config/.env")
API_KEY = os.getenv("TRADIER_API_KEY")

# Define the User Profile endpoint
profile_endpoint = "https://api.tradier.com/v1/user/profile"

# Set up headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

# Make the request to get user profile
response = requests.get(profile_endpoint, headers=headers)
json_response = response.json()

# Check the status and print the response
if response.status_code == 200:
    print("Profile data retrieved successfully.")
    print(json_response)
    # Access account ID directly
    account_id = json_response['profile']['account']['account_number']
    print("Account ID:", account_id)
else:
    print(f"Failed to retrieve profile data. Status code: {response.status_code}")
    print(json_response)