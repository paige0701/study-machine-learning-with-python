from numpy import array

# https://machinelearningmastery.com/index-slice-reshape-numpy-arrays-machine-learning-python/

# list of data
data = [11, 22, 33, 44, 55]

# array of data
data = array(data)
print(data)
print(type(data))

# two dimensional arrays
data2 = [[11, 22], [33, 44], [55, 66]]
# array of data
data2 = array(data2)
print(data2)
print(type(data2))

# indexing 2 dimensional arrays with comma
print(data2[0, 0])  # 11

# if you are interested in all items in the first row, leave the second dimension index empty
print(data2[0, ])  # [11, 22]

# array slicing data[from:to]
# access all data in array
print(data[:])  # [11,22,33,44,55]

# using negative indexes in slices
print(data[-2:])  # [44, 55]

# slicing in two dimensions
test = array([[11, 22, 33],
              [44, 55, 66],
              [77, 88, 99]])
# separate data
X, y = test[:, :-1], test[:, -1]
print(X)
print(y)
