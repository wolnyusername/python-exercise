import pandas
import pandas as pd


auto = pd.read_csv('Automobile_data.csv')
# From the given dataset print the first and last five rows
print(auto.head(5))
print(auto.tail(5))
# Find the most expensive car company name
company_price = auto[["company", "price"]][auto.price == auto['price'].max()]
# Print All Toyota Cars details
# first way
toyota_cars = auto[auto["company"] == "toyota"]
# second way
tot = auto.groupby('company')
toy = tot.get_group('toyota')
# Count total cars per company
print(auto["company"].value_counts())
# Find each company’s Higesht price car
print(tot['price'].max())
# Find the average mileage of each car making company
print(tot['average-mileage'].mean())
# Sort all cars by Price column
print(auto.sort_values(by="price", ascending=False))
# Concatenate two data frames using the following conditions, create two data frames using the following two dictionaries.
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
df = pandas.DataFrame(data=[GermanCars, japaneseCars])
ger_cars = pd.DataFrame.from_dict(GermanCars)
jap_cars = pd.DataFrame.from_dict(japaneseCars)
car = pd.concat([ger_cars,jap_cars], keys=("germany","japan"))
print(car)
# Merge two data frames using the following condition
# Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
car_with_price = pd.DataFrame.from_dict(Car_Price)
car_with_horsepower = pd.DataFrame.from_dict(car_Horsepower)
print(car_with_price.merge(car_with_horsepower))