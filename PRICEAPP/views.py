from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import time
# Create your views here.
def home(request):
    # urls for coinbase api
    url_btc_buy = 'https://api.coinbase.com/v2/prices/BTC-USD/buy'
    url_btc_sell = 'https://api.coinbase.com/v2/prices/BTC-USD/sell'
    url_eth_buy = 'https://api.coinbase.com/v2/prices/ETH-USD/buy'
    url_eth_sell = 'https://api.coinbase.com/v2/prices/ETH-USD/sell'

    # urls for gemini api
    url_gemini_btc = 'https://api.gemini.com/v1/pubticker/btcusd'
    url_gemini_eth = 'https://api.gemini.com/v1/pubticker/ethusd'

    coin_currency = 'BTC'
    coin_currency1 = 'ETH'

    # requests for coinbase api
    data = requests.get(url_btc_buy.format(coin_currency)).json()
    data1 = requests.get(url_btc_sell.format(coin_currency)).json()
    data2 = requests.get(url_eth_buy.format(coin_currency1)).json()
    data3 = requests.get(url_eth_sell.format(coin_currency1)).json()

    # requests for gemini api 
    data4 = requests.get(url_gemini_btc.format(coin_currency)).json()
    data5 = requests.get(url_gemini_eth.format(coin_currency1)).json()


    coin_btc = {
        'Currency': coin_currency,
        'buying_price': data['data']['amount'],
        'selling_price': data1['data']['amount'],
    }
    coin_eth = {
        'Currency1': coin_currency1,
        'buying_price': data2['data']['amount'],
        'selling_price': data3['data']['amount'],

    }
    gemini_btc = {
        'buying_price': data4['ask'],
        'selling_price': data4['bid'],
    }
    gemini_eth = {
        'buying_price': data5['ask'],
        'selling_price': data5['bid'],
    }
    
    context = {'coin_btc' : coin_btc, 'coin_eth' : coin_eth, 'gemini_btc' : gemini_btc, 'gemini_eth' : gemini_eth}
    
    return render(request,'home.html', context)


