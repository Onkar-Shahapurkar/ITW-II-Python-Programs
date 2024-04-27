import inline as inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/91932/PycharmProjects/ITW-II/PR 9/company_sales_data.csv')

month_list = df['month_number'].tolist()
tooth_paste_sales_data = df['toothpaste'].tolist()
# Your code here
fig, ax = plt.subplots()
ax.scatter(month_list, tooth_paste_sales_data, label='Tooth Paste Sales Data')

ax.set(title='Tooth Paste Sales Data',
       xlabel='Month Number',
       ylabel='Number of Units Sold',
       xticks=month_list)

ax.legend(loc='upper left')
ax.grid(linestyle='--')
plt.show()