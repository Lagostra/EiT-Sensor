import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/data.csv', parse_dates=True, index_col=[0])

resample_1m = data.resample('1T')
resample_1m = resample_1m.mean()
resample_1m.to_csv('data/data-1m.csv')

resample_5m = data.resample('5T')
resample_5m = resample_5m.mean()
resample_5m.to_csv('data/data-5m.csv')

resample_10m = data.resample('10T')
resample_10m = resample_10m.mean()
resample_10m.to_csv('data/data-10m.csv')