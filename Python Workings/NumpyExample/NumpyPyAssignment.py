import numpy as np

def assginment1():
    ## ASSIGNMENT 1 - Array Creation and Manipulation
    # Create a NumPy array of shape (5, 5) filled with random integers
    array = np.random.randint(1, 21, size=(5, 5))
    print("Original array:")
    print(array)
    print()
    # Replace all the elements in the third column with 1
    array[:, 2] = 1
    print("Modified array:")
    print(array)
    print()
    # Create a NumPy array of shape (4, 4) with values from 1 to 16
    array = np.arange(1, 17).reshape((4, 4))
    print("Original array:")
    print(array)
    print()
    # Replace the diagonal elements with 0
    np.fill_diagonal(array, 0)
    print("Modified array:")
    print(array)


def assginment2a():
    ## ASSIGNMENT 2 - Array Indexing and Slicing
    # Create a NumPy array of shape (6, 6) with values from 1 to 36
    array = np.arange(1, 37).reshape((6, 6))
    print("Original array:")
    print(array)
    print()
    # Extract the sub-array
    sub_array = array[2:5, 1:4]
    print("Sub-array:")
    print(sub_array)
    print()


def assignment2b():
    # Create a NumPy array of shape (5, 5) with random integers
    array = np.random.randint(1, 21, size=(5, 5))
    #array = inputArray
    print("Original array:")
    print(array)
    print()
    # Extract the elements on the border
    border_elements = np.concatenate((array[0, :], array[-1, :], array[1:-1, 0], array[1:-1, -1]))
    print("Border elements:")
    print(array[0, :])
    print(array[-1, :])
    print(array[1:-1, 0])
    print(array[1:-1, -1])
    print(border_elements)
    print()
    print("Border Elements removing duplicates :")
    arraySet= set(border_elements)
    for x in arraySet:
        print(x)


def assignment3a():
    ## ASSIGNMENT 3- Array Operations
    array1 = np.random.randint(1, 21, size=(3, 4))
    array2 = np.random.randint(1, 21, size=(3, 4))
    #array = inputArray
    print("Array 1:")
    print(array1)
    print()
    print("Array 2:")
    print(array2)
    print()
    print("Adding Array 1 and Array 2 :")
    print(array1+array2)
    print()
    print("Substracting Array 1 and Array 2 :")
    print(array1-array2)
    print()
    print("Multiply Array 1 and Array 2 :")
    print(array1*array2)
    print()
    print("Division of Array 1 and Array 2 :")
    print(array1/array2)


def assignment3b():
    ## ASSIGNMENT 3- Array Operations
    array1 = np.random.randint(1, 21, size=(3, 6))
    print("Array 1:")
    print(array1)
    print()
    print("Column-wise Sum")
    print(np.sum(array1, axis=0)) # COLUMN WISE
    print("Row-wise Sum")
    print(np.sum(array1, axis=1)) # ROW WISE


def assignment4a():
    ## ASSIGNMENT 4 - Statistical Operations
    array = np.random.randint(1, 21, size=(5, 5))
    print("Array :")
    print(array)
    print()
    # Compute the statistical values
    mean = np.mean(array)
    median = np.median(array)
    std_dev = np.std(array)
    variance = np.var(array)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)
    print("Variance:", variance)

def assignment4b():
    # Create a NumPy array of shape (3, 3) with values from 1 to 9
    array = np.arange(1, 10).reshape((3, 3))
    print("Original array:")
    print(array)

    # Normalize the array
    mean = np.mean(array)
    std_dev = np.std(array)
    normalized_array = (array - mean) / std_dev

    print("Normalized array:")
    print(normalized_array)