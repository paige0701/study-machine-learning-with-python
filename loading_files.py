import csv
import numpy
import pandas

# https://machinelearningmastery.com/load-machine-learning-data-python/

filename = 'pima-indians-diabetes.data.csv'
directory = f'files/{filename}'
raw_data = open(directory, 'r')

# reading files with numpy
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)


# read file with pandas
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(directory, names=names)
print(data.shape)