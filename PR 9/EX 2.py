import inline as inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/91932/PycharmProjects/ITW-II/PR 9/company_sales_data.csv')

profit_list = df['total_profit'].tolist()
month_list = df['month_number'].tolist()

fig, ax = plt.subplots()
ax.plot(month_list, profit_list, 'r--o', mfc='k', label='Profit Data of Last Year')

ax.set(xticks=month_list,
       yticks=np.arange(1e5, 6e5, 1e5),
       xlabel='Month Number',
       ylabel='Profit in Dollar',
       title='Company Profit per Month')
ax.legend(loc='lower right')
plt.show()