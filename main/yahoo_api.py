import yfinance as yf
from os import path
import pandas as pd
import datetime
from dateutil.parser import parse


def load(ticker):
    hourly_filename = f"../data/{ticker}_daily.csv"

    if path.exists(hourly_filename):
        hourly_chart = pd.read_csv(hourly_filename)
        last_date = hourly_chart['Date'].get_values()[-1]
        if parse(last_date).date() < datetime.date.today():
            hourly_hist = fetch_daily(ticker, last_date)
            hourly_chart.append(hourly_hist)
            save_to_csv(hourly_chart, hourly_filename)
    else:
        hourly_chart = fetch_daily(ticker)
        save_to_csv(hourly_chart, hourly_filename)

    return hourly_chart


def fetch_daily(ticker, start_date=None):
    stock_info = yf.Ticker(ticker)
    if start_date is not None:
        hist = stock_info.history(start=start_date)
    else:
        hist = stock_info.history(period='max')

    return hist


def save_to_csv(data, filename):
    pd.DataFrame(data).to_csv(filename)
