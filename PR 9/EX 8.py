import inline as inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/91932/PycharmProjects/ITW-II/PR 9/company_sales_data.csv')

data = {
'Face Cream': df['facecream'].sum(),
'Face Wash': df['facewash'].sum(),
'Tooth Paste': df['toothpaste'].sum(),
'Bathing Soap': df['bathingsoap'].sum(),
'Shampoo': df['shampoo'].sum(),
'Moisturizer': df['moisturizer'].sum()
}
fig, ax = plt.subplots()
ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
ax.set(title='Sales Data')

ax.axis('equal')
ax.legend(loc='lower right')
plt.show()