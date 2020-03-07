import requests
import csv

url = 'https://www.bitmex.com/api/v1/trade/bucketed?binSize=1m&partial=false&symbol=XBT&count=1000&reverse=true'

r = requests.get(url).json()
crypto_data = []
for i in r:
    crypto_data.append(int(i['close']))

with open('data/crypto/{}.csv'.format('latest'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(crypto_data)