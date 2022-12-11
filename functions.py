import requests

def get_json_request(url):
    return requests.get(url).json()

def get_crypto_price(data, currency='USD'):
    return data['quotes'][currency]['price']