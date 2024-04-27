import inline as inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/91932/PycharmProjects/ITW-II/PR 9/company_sales_data.csv')

month_list = df['month_number'].tolist()
bathing_soap_sales_data = df ['bathingsoap'].tolist()
fig, ax = plt.subplots()
ax.bar(month_list, bathing_soap_sales_data)

ax.set(title='Bathing Soap Sales Data',
       xlabel='Month Number',
       ylabel='Sales Units in Number',
       xticks=month_list)

ax.grid(ls='--')
fig.savefig('bathingsoap.png', dpi=80)
plt.show()
