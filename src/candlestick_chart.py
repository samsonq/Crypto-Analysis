import ccxt
import plotly.graph_objects as go
import pandas as pd
import datetime

# exchange_id = 'binance'
# exchange_id = 'bitmex'
exchange_id = 'bitfinex'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'enableRateLimit': True,
})
# symbol = 'ETH/BTC'
symbol = 'BTC/USD'

print(exchange.has['fetchOHLCV'])
limit = 1000
# binance starts at 1500004800000, july 14, 2017 04:00:00 AM (GMT)
# bitmex starts at 1443182400000, september 25, 2015 12:00:00 PM
# bitfinex starts at 1364774820000, april 1, 2013 12:07:00 AM
since = 0
timestamp = datetime.datetime.fromtimestamp(since / 1000)

ohlcv = exchange.fetch_ohlcv(symbol, '1m', limit=limit, since=since)
df = pd.DataFrame(ohlcv, columns=['UTC', 'Open', 'High', 'Low', 'Close', 'Volume'])
df['UTC'] = df['UTC'].map(lambda time: datetime.datetime.fromtimestamp(time / 1000).strftime('%Y-%m-%d %H:%M:%S'))

fig = go.Figure(data=[go.Candlestick(x=df['UTC'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

fig.show()