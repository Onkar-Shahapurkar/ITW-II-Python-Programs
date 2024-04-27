import inline as inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/91932/PycharmProjects/ITW-II/PR 9/company_sales_data.csv')

profit_list = df['total_profit'].tolist()
profit_range = [15e4, 17e4, 20e4, 225e3, 25e4, 30e4, 35e4]
labels = ['Low', 'Average', 'Good', 'Best', 'abc']
fig, ax = plt.subplots()
ax.hist(profit_list, profit_range, label='Profit data')

ax.set(title='Profit Data',
       xlabel='Profit Range in Dollar',
       ylabel='Actual Profit in Dollar',
       xticks=profit_range)

ax.legend(loc='upper left')
plt.show()
