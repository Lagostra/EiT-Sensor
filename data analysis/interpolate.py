import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/data.csv', parse_dates=True, index_col=[0])

resample = data.resample('10T')
resample = resample.mean()

resample.to_csv('data/data-10m.csv')
