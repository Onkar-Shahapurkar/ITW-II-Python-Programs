import pandas as pd

# Load the dataset
url = "C:/Users/91932/PycharmProjects/ITW-II/PR 10/Automobile_data.csv"
auto_data = pd.read_csv(url)

# a. Print the first and last five rows
print("First five rows:")
print(auto_data.head())

print("\nLast five rows:")
print(auto_data.tail())

# b. Find the most expensive car company name
most_expensive_company = auto_data.loc[auto_data['price'].idxmax(), 'company']
print("\nMost expensive car company:", most_expensive_company)

# c. Print all Toyota cars details
toyota_cars = auto_data[auto_data['company'] == 'toyota']
print("\nToyota Cars Details:")
print(toyota_cars)

# d. Count total cars per company
cars_per_company = auto_data['company'].value_counts()
print("\nTotal cars per company:")
print(cars_per_company)

# e. Find the average mileage of each car making company
average_mileage = auto_data.groupby('company')['average-mileage'].mean()
print("\nAverage mileage of each car making company:")
print(average_mileage)

