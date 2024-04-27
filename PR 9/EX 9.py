import inline as inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/91932/PycharmProjects/ITW-II/PR 9/company_sales_data.csv')

month_list = df['month_number'].tolist()
bathing_soap_sales_data = df['bathingsoap'].tolist()
face_wash_sales_data = df['facewash'].tolist()
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(month_list, bathing_soap_sales_data, 'k-o', lw=3)
ax1.set(title='Sales Data of Bathing Soap')
ax2.plot(month_list, face_wash_sales_data, 'r-o', lw=3)

ax2.set(title='Sales Data of Face Wash',
        xlabel='Month Number',
        ylabel='Sales Units in Number',
        xticks=month_list)
plt.show()