import inline as inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/91932/PycharmProjects/ITW-II/PR 9/company_sales_data.csv')

month_list = df['month_number'].values
face_cream_sales_data = df['facecream'].tolist()
face_wash_sales_data = df['facewash'].tolist()
fig, ax = plt.subplots()
bar_width = 0.25
offset = 0.125

ax.bar(month_list-offset, face_cream_sales_data, width=bar_width, label='Face Cream Sales Data')
ax.bar(month_list+offset, face_wash_sales_data, width=bar_width, label='Face Wash Sales Data')

ax.set(title='Face Wash and Face Cream Sales Data',
       xlabel='Month Number',
       ylabel='Sales Units in Number',
       xticks=month_list)

ax.grid(ls='--')
ax.legend(loc='upper left')
plt.show()