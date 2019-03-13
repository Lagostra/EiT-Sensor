import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_context('paper')
sns.set_palette('muted')

start = '2019-03-06 09:00'
end = '2019-03-06 19:00'

data_raw = pd.read_csv('data/data.csv', index_col=0, parse_dates=True)
data_raw = data_raw[start:end]
data_raw.plot()
plt.title('Raw data')
plt.show()

data_1m = pd.read_csv('data/data-1m.csv', index_col=0, parse_dates=True)
data_1m = data_1m[start:end]
data_1m.plot()
plt.title('1m aggregate')
plt.show()

data_5m = pd.read_csv('data/data-5m.csv', index_col=0, parse_dates=True)
data_5m = data_5m[start:end]
data_5m.plot()
plt.title('5m aggregate')
plt.show()

data_10m = pd.read_csv('data/data-10m.csv', index_col=0, parse_dates=True)
data_10m = data_10m[start:end]
data_10m.plot()
plt.title('10m aggregate')
plt.show()
