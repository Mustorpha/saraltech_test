"""
The Python Script performs the following tasks:

    1. Load provided dataset into a pandas dataframe
    2. Perform data cleaning and preprocessing as necessary
    3. Calculate the average, median and standard deviation of the `price` column
    4. Identify and remove any outliers from the dataset
    5. Export the cleaned dataset into a new CSV file
"""

import pandas as pd

df = pd.read_csv('data.csv')
df.dropna(subset=['price'], inplace=True)

avg_price = df['price'].mean()
median_price = df['price'].median()
std_price = df['price'].std()

print(f"Average Price: ${avg_price:.2f}")
print(f"Median Price: ${median_price:.2f}")
print(f"Standard Deviation: ${std_price:.2f}")

#identifing outliers using inter-quartile range of the prices
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]

df_cleaned = df[~df.index.isin(outliers.index)]
df_cleaned.to_csv('cleaned_data.csv', index=False)
