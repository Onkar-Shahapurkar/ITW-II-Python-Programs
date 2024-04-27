import inline as inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/91932/PycharmProjects/ITW-II/PR 9/company_sales_data.csv')

month_list = df['month_number'].tolist()
face_cream_sales_data = df['facecream'].tolist()
face_wash_sales_data = df['facewash'].tolist()
tooth_paste_sales_data = df['toothpaste'].tolist()
bathing_soap_sales_data = df['bathingsoap'].tolist()
shampoo_sales_data = df['shampoo'].tolist()
moisturizer_sales_data = df['moisturizer'].tolist()

fig, ax = plt.subplots()

ax.plot(month_list, face_cream_sales_data, '-o', label='Face Cream Sales Data')
ax.plot(month_list, face_wash_sales_data, '-o', label='Face Wash Sales Data')
ax.plot(month_list, tooth_paste_sales_data, '-o', label='Tooth Paste Sales Data')
ax.plot(month_list, bathing_soap_sales_data, '-o', label='Bathing Soap Sales Data')
ax.plot(month_list, shampoo_sales_data, '-o', label='Shampoo Sales Data')
ax.plot(month_list, moisturizer_sales_data, '-o', label='Moisturizer Sales Data')

ax.set(xticks=month_list,
       yticks=[1e3, 2e3, 4e3, 6e3, 8e3, 1e4, 12e3, 15e3, 18e3],
       xlabel='Month number',
       ylabel='Sales unit in number',
       title='Sales Data')
ax.legend(loc='upper right')
plt.show()