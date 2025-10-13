# Customer Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV 
file_path = r"C:\Users\Maryam Bano\Desktop\customer_info.csv"
df = pd.read_csv(file_path)

# View first few rows
print("First 5 rows of data:")
print(df.head(), "\n")


# Total quantity sold per product
quantity_per_product = df.groupby('Product')['Quantity'].sum()


# 6️Simple visualizations

# Bar chart: total quantity sold per product
quantity_per_product.plot(kind='bar', title='Total Quantity Sold per Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity')
plt.show()


