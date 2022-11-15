import pandas
import pandas as pd


auto = pd.read_csv('Automobile_data.csv')
# From the given dataset print the first and last five rows
auto.head(5)
auto.tail(5)
# Find the most expensive car company name
company_price = auto[["company", "price"]][auto.price == auto['price'].max()]
# Print All Toyota Cars details
# first way
toyota_cars = auto[auto["company"] == "toyota"]
# second way
tot = auto.groupby('company')
toy = tot.get_group('toyota')
# Count total cars per company
auto["company"].value_counts()
# Find each company’s Higesht price car
tot['price'].max()
# Find the average mileage of each car making company
tot['average-mileage'].mean()
# Sort all cars by Price column
auto.sort_values(by="price", ascending=False)
# Concatenate two data frames using the following conditions, create two data frames using the following two dictionaries.
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
df = pandas.DataFrame(data=[GermanCars, japaneseCars])
ger_cars = pd.DataFrame.from_dict(GermanCars)
jap_cars = pd.DataFrame.from_dict(japaneseCars)
car = pd.concat([ger_cars,jap_cars], keys=("germany","japan"))
# Merge two data frames using the following condition
# Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
car_with_price = pd.DataFrame.from_dict(Car_Price)
car_with_horsepower = pd.DataFrame.from_dict(car_Horsepower)
car_with_price.merge(car_with_horsepower)

# Create a pandas series from each of the items below: a list, numpy and a dictionary
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
list_series = pd.Series(mylist)
array_series = pd.Series(myarr)
dict_series = pd.Series(mydict)
# Convert the series dict_series into a dataframe with its index as another column on the dataframe.
dict_frame = dict_series.to_frame().reset_index()
# Combine list_series and array_series to form a dataframe.
list_and_array_data_frame = pd.DataFrame({"col 1":mylist, "col 2":myarr})
# Give a name to the series list_series calling it ‘alphabets’.
list_series.name = "alphabets"
# From ser1 remove items present in ser2.
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser1_removed = ser1[~ser1.isin(ser2)]
# Get items common to both ser1 and ser2.
common_items = ser1[ser1.isin(ser2)]
# Get all items of ser1 and ser2 not common to both.
ser_u = pd.Series(np.union1d(ser1, ser2))
ser_i = pd.Series(np.intersect1d(ser1, ser2))
all_not_common = ser_u[~ser_u.isin(ser_i)]
#  Compute the minimum, 25th percentile, median, 75th, and maximum of ser.
ser_to_describe = pd.Series(np.random.normal(10, 5, 25))
ser_to_describe.describe()
# Calculte the frequency counts of each unique value ser.
ser_to_count_unique = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser_to_count_unique.value_counts()
