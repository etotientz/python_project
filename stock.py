import pandas as pd
'''import quandl
a=quandl.get("NSE/RELIANCE", start_date="2016-06-12")
print a.head()
a['%_CHANGE']=(a['Close']-a['Open']) % a['Open']
#a=a[['%_CHANGE']]
print a '''
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

start=datetime.datetime(2012,1,1)
end=datetime.datetime(2015,1,1)
df =web.DataReader("XOM","yahoo",start,end)
print df.head()
df['Low'].plot()
plt.legend()
plt.show()