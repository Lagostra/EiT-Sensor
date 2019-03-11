import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_context('paper')
sns.set_palette('muted')

data = pd.read_csv('data/data.csv', index_col=0, parse_dates=True)

data.plot()
plt.show()
