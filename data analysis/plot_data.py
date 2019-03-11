import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/data.csv', index_col=0, parse_dates=True)

data.plot()
plt.show()
