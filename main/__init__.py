import pandas as pd

import yahoo_api as yahoo
import data_wragle as dw

ticker = "DJI"
data = yahoo.load(ticker)

print(data)
features_considered = ['Open', 'High', 'Low', 'Close', 'Volume']
data_w_noise = pd.DataFrame(data)
data_w_noise[features_considered] = pd.DataFrame(dw.add_noise(data[features_considered]))

print(data_w_noise)

