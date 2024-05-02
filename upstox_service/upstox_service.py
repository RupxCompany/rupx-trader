import requests
import os

# Access the access token defined in settings
UPSTOX_ACCESS_TOKEN = os.getenv('UPSTOX_ACCESS_TOKEN')


class UpstoxService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.access_token = UPSTOX_ACCESS_TOKEN
        self.base_url = 'https://api.upstox.com/v2'

    def fetch_historic_candle_data(self, instrument_key, interval, from_date, to_date):
        url = f"{self.base_url}/historical-candle/{instrument_key}/{interval}/{to_date}/{from_date}"
        headers = {
            'x-api-key': self.api_key,
            'Authorization': f"Bearer {self.access_token}"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching historic candle data: {response.text}")
            return None

    def fetch_intraday_candle_data(self, instrument_key, interval):
        url = f"{self.base_url}/historical-candle/intraday/{instrument_key}/{interval}"
        headers = {
            'x-api-key': self.api_key,
            'Authorization': f"Bearer {self.access_token}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching intraday candle data: {response.status_code}")
            return None

    def fetch_full_market_quote(self, instrument_keys):
        url = f"{self.base_url}/market-quote/quotes?instrument_key={instrument_keys}"
        params = {
            'instrument_keys': ','.join(instrument_keys)
        }
        headers = {
            'x-api-key': self.api_key,
            'Authorization': f"Bearer {self.access_token}"
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching full market quote: {response.status_code}")
            return None
