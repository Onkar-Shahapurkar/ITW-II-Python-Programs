import inline as inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/91932/PycharmProjects/ITW-II/PR 9/company_sales_data.csv')

month_list = df['month_number'].tolist()
data = {
'Face Cream': df['facecream'].values,
'Face Wash': df['facewash'].values,
'Tooth Paste': df['toothpaste'].values,
'Bathing Soap': df['bathingsoap'].values,
'Shampoo': df['shampoo'].values,
'Moisturizer': df['moisturizer'].values
}

fig, ax = plt.subplots()
ax.stackplot(month_list, data['Face Cream'], data['Face Wash'], data['Tooth Paste'],
data['Bathing Soap'], data['Shampoo'], data['Moisturizer'],
             labels=data.keys(),
             colors=['m', 'c', 'r', 'k', 'g', 'y'])

ax.set(title='All Product Sales Data',
       xlabel='Month Number',
       ylabel='Sales Units in Number')
ax.legend(loc='upper left')
plt.show()