import plotly.graph_objects as go
import pandas as pd
import datetime

bitfinex_start = 1364774820000  # bitfinex btc/usd starts at 1364774820000, april 1, 2013 12:07:00 AM


def candlestick_from_csv(csv, start_time, end_time):
    time_frame = 60 * 1000  # milliseconds per minute
    start_index = (start_time - bitfinex_start) / time_frame
    end_index = (end_time - bitfinex_start) / time_frame

    df = pd.read_csv(csv)
    df = df.iloc[int(start_index):int(end_index)]
    df['UTC'] = df['UTC'].map(lambda time: datetime.datetime.fromtimestamp(time / 1000).strftime('%Y-%m-%d %H:%M:%S'))

    fig = go.Figure(data=[go.Candlestick(x=df['UTC'],
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])

    fig.show()


candlestick_from_csv('bitfinex_btc_data.csv', 1388534400*1000, 1391212800*1000)
