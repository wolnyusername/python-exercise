import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Create a 4X2 integer array and Prints its attributes
def create_first_array():
    x = np.empty([4,2], dtype=np.uint16)
    print(x)
    print(f"Array shape is: {x.shape}")
    print(f"Array dimensions are {x.ndim}")
    print(f"Length of element in bytes {x.itemsize}")


# Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
def create_second_array():
    x = np.arange(100,200,10)
    x = x.reshape(5,2)
    print(x)


# Following is the provided numPy array. Return array of items by taking the third column from all rows
def third_column():
    sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
    new_array = np.hsplit(sampleArray, 3)[2]
    print(new_array)


#Return array of odd rows and even columns from below numpy array
def odd_row_even_columns():
    sampleArray = np.array([[3, 6, 9, 12], [15, 18, 21, 24],
                               [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
    print(sampleArray)
    new_array = sampleArray[::2, 1::2]
    print(new_array)


# Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element
def add_arrays():
    arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
    arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
    expected = np.add(arrayOne,arrayTwo)
    value = np.square(expected)
    print(value)


# Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
def split_in_four():
    result_array = np.arange(10,34)
    result_array = result_array.reshape(8,3)
    print(np.split(result_array, 4))


# Print max from axis 0 and min from axis 1 from the following 2-D array.
def max_and_min_of_array():
    sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    print(sampleArray)
    print(np.amax(sampleArray, axis=0))
    print(np.amin(sampleArray, axis=1))


# Delete the second column from a given array and insert the following new column in its place.
def del_and_insert_column():
    sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    newColumn = np.array([[10, 10, 10]])
    print(sampleArray)
    sampleArray = np.delete(sampleArray, obj=1, axis=1)
    sampleArray = np.insert(sampleArray, obj=1, values=newColumn, axis=1)
    print(sampleArray)


# Create two 2-D arrays and Plot them using matplotlib
def plot_2_arrays():
    sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    sampleArray2 = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
    fig, ax = plt.subplots()
    ax.plot(sampleArray,sampleArray2)
    plt.show()