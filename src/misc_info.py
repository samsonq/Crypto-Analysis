import ccxt
import pandas as pd


def get_exchange_symbols(exchange_id):
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class()
    exchange.load_markets()
    print(exchange.symbols)
    print(exchange.has['fetchOHLCV'])


def exchange_start_date(exchange_id, symbol):
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'enableRateLimit': True,
    })

    limit = 5
    since = 0

    ohlcv = exchange.fetch_ohlcv(symbol, '1m', limit=limit, since=since)
    df = pd.DataFrame(ohlcv, columns=['UTC', 'Open', 'High', 'Low', 'Close', 'Volume'])
    print(df.head(5))


# exchange_start_date('bitfinex', 'BSV/USD')
df = pd.read_csv('bitmex_btc_data.csv')
print(None in df)