import numpy as np

# a = [[1, 2, 3], [4, 5, 6]] # two dimensional array

# print(np.array(a)) # prints that array

# np_array = np.array(a) # creates ndarray obj

# print(np_array.dtype) # prints the type of ndarry obj i.e type of elemnts in that array

# arr2 = np_array.astype(np.int32) # to change the type of array
# print(arr2.dtype)
# print(arr2.size) #returns the number of elements in array

# print(arr2.ndim) # returns the dimension of array

# print(arr2.shape) # gives number of elements along each dimension
# print(len(arr2.shape)) # gives number of dimensions array have

# print(np.ones((4,6), )) #printing array containg all ones
# print(np.ones((4,6), dtype=np.int_)) #same as above but this time specifying datatype of elements
# np.zeros((2,2)) 

# We can use these functions to create arrays with arbitrary values, e.g., we can create an array containing the values 99 as follows:
# print(np.zeros((3,3))+99)

# print(np.empty((2,2))) # creates empty array
# print(np.eye(3)) # creates identity matrix
# print(np.diag((3,5,6))) # creates diagonal matrix
# print(np.arange(1,11)) #works like pythons range fucntion
# print(np.arange(1., 11., 0.1)) #third arguements is steps it gives difference between numbers default is 1
# print(np.linspace(1,20, num=15)) # gives exact numbers specified in third argument between first and second number with even space

arr = np.array([1,2,3,4,5,6,7])
# print(arr[1]) # accessing array with index
# print(arr[2:5]) # slicing array

# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2[0, 2]) # first element represents row, second element represents column
# print(arr2[:,2]) # both rows second column
# print(arr2[:,:2]) # both rows till second column

# VECTORIZATAION, numpy has ufuncs which are functions that we can use to perform mathematical operations on ndarrays
# we have add, subtract, divide, multiply, power, and exp and many more
# we can also use sign directly like +, -, /, *, and **

# arry = np.add(arr,15)
# print(arry)
# print(arr+1)
# print(np.sqrt(arr))

# REDUCE

print(np.add.reduce(arr)) # performs addition all elements in array

ary = np.array([[1, 2, 3], 
                [4, 5, 6]]) 
# axis 0 is horizontal axis
# axis 1 is vertical axis
print(np.add.reduce(ary, axis=0)) # rolling over the 1st axis, axis 0

# np.mean (computes arithmetic mean or average)
# np.std (computes the standard deviation)
# np.var (computes variance)
# np.sort (sorts an array)
# np.argsort (returns indices that would sort an array)
# np.min (returns the minimum value of an array)
# np.max (returns the maximum value of an array)
# np.argmin (returns the index of the minimum value)
# np.argmax (returns the index of the maximum value)
# np.array_equal (checks if two arrays have the same shape and elements)