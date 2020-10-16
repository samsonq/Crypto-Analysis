import ccxt
import pandas as pd


def get_data_from(exchange_id, start_time, end_time, crypto_pair): # start and end time in unix timestamp (milliseconds)
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'enableRateLimit': True,
    })

    if exchange.has['fetchOHLCV']:
        limit = 5000  # number of entries of data
        time_frame = 60 * 1000  # 1m = 60000 ms

        ohlcv = exchange.fetch_ohlcv(crypto_pair, '1m', limit=limit, since=start_time)
        df = pd.DataFrame(ohlcv, columns=['UTC', 'Open', 'High', 'Low', 'Close', 'Volume'])
        start_time += limit * time_frame
        print(str(limit) + " entries fetched...")

        while start_time < end_time:
            ohlcv = exchange.fetch_ohlcv(crypto_pair, '1m', limit=limit, since=start_time)
            df = df.append(pd.DataFrame(ohlcv, columns=['UTC', 'Open', 'High', 'Low', 'Close', 'Volume']),
                           ignore_index=True)
            start_time += limit * time_frame
            print(str(limit) + " entries fetched...")
        return df


df = get_data_from('bitfinex', 1542108300000, 1593713972*1000, 'BCH/USD')
df.to_csv('bitfinex_bch_data.csv', index=False)
