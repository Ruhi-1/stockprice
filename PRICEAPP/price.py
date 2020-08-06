import requests
import json
import time

while True:
    response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
    response1 = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell')

    response2 = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy')
    response3 = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/sell')

  # getting data for bitcoin buying price 
    data = response.json()
    currency = data["data"]["base"]
    buying_price = data["data"]["amount"]
    
  # getting data for bitcoin selling price
    data = response1.json()
    selling_price = data["data"]["amount"]

  # getting data for ethereum buying price
    data = response2.json()
    currency1 = data["data"]["base"]
    buying_price1 = data["data"]["amount"]

  # getting data for ethereum selling price 
    data = response3.json()
    selling_price1 = data["data"]["amount"]

  # print function for bitcoin buying and selling price
    print(f"Currency: {currency}, Buying Price: {buying_price}, Selling Price: {selling_price}")

  # print function for ethereum buying ans selling price 
    print(f"Currency: {currency1}, Buying Price: {buying_price1}, Selling Price: {selling_price1}")
    time.sleep(15)