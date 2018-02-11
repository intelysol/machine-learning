import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def price_historical(coin, campare_with, all_data=False, limit=563, aggregate=1, exchange=''):
    #the base url for getting the history data online
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(coin.upper(), campare_with.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    if all_data:
        url += '&allData=true'
    #send the request for data
    page = requests.get(url)
    #convert to the json format
    data = page.json()['Data']
    #convert to the pandas dataframe
    df = pd.DataFrame(data)
    #convert the time to timestamp
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    #filter the data for year 2017 and return
    return df

#Retrive the Bitcoin price history
btc_data = price_historical('BTC', 'USD', all_data=True)

#Plot the Bitcoin data
plt.plot(btc_data.timestamp, btc_data.high,label="BTC",color="b")
#labeling the chart
plt.xlabel("Year")
plt.ylabel("Price")
#title the graph
plt.title("Price of BTC\nBetween the Year 2017")
#show the graph
plt.show()
