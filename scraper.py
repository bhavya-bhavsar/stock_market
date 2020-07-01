import requests
import json
from credentials import  key
from tqdm import tqdm
import time
def search(symbol):
    URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + symbol + "&outputsize=full&apikey=" + key
    html = requests.get(URL).json()
    return html

watch_list = ['GOOGL', 'IBM', 'AAPL', 'FB', 'TWTR', 'TSLA', 'MSFT']
for company in tqdm(watch_list):
    time.sleep(5)
    data = search(company)
    data = data['Time Series (Daily)']
    fp = open('Data/' + company + '.json', 'w')
    json.dump(data, fp)
    fp.close()
# print(search('GOOGL')['Time Series (Daily)'])