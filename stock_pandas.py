import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib as plt

gld = pd.read_csv('GLD.csv')

#Discard unneeded data
gld_close = pd.DataFrame(gld.Close)
#print(gld_close.head())

gld_close['MA_9'] = gld_close.Close.rolling(9).mean()
gld_close['MA_21'] = gld_close.Close.rolling(21).mean()

#print(gld_close.head())

#plt.figure(figsize=(15,10))
plt.grid(True)
plt.plot(gld_close['Close'],label='GLD')
plt.plot(gld_close['MA_9'],label='MA 9 day')
plt.plot(gld_close['MA_21'],label='MA 21 day')
plt.legend(log=2)
plt.show()
