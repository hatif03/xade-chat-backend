import requests
from requests import RequestException
import json
from openbb_terminal.sdk import openbb

def get_coin_data(coin_name):
    try:
        # Make a GET request to the API
        response = requests.get(url=f"https://api.coingecko.com/api/v3/coins/markets", params={"vs_currency": "usd", "ids": f"{coin_name}"}) #

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the JSON response
            return response.content
            return (f"The live data about {coin_name}: {json.dumps(response.json())}")
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except RequestException as e:
        # Handle exceptions (e.g., timeout, connection error)
        print(f"Error: {e}")
        return None

