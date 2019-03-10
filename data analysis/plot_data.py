import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/data.csv', parse_dates=[0])

data.plot(x='time', y='co2')
plt.show()
