import requests
import ephem

# Function to get Ethereum price from CoinGecko API
def get_eth_price():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum'
    response = requests.get(url).json()
    return response[0]['current_price']

# Function to get lunar cycle information using PyEphem
def get_lunar_phase():
    moon = ephem.Moon()
    moon.compute()
    return ephem.Moon.phase(moon)

# Loop to continuously track Ethereum price and lunar cycles
while True:
    eth_price = get_eth_price()
    lunar_phase = get_lunar_phase()
    print(f'Ethereum price: ${eth_price:.2f}, Lunar phase: {lunar_phase:.2f}')
