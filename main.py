import requests
import json
endPoint = 'https://api.coin.z.com/public'
path = '/v1/ticker?symbol=BTC'
response = requests.get(endPoint + path)
print('現在のビットコインの価格は', response.json()['data'][0]['last'],'円です')