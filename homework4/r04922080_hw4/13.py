import numpy as np
import random
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv

Lambda = 11.26
size = 200
Dimension_Add_1 = 3
test_size = 1000

def sign(a):
	if a >= 0:
		return 1
	else:
		return -1

def main():

	f = open("hw4_train.dat", "r")
	X = np.zeros(shape=(size, Dimension_Add_1))
	y = np.zeros(shape=(size, 1))
	X = np.asmatrix(X)
	y = np.asmatrix(y)
	num = 0
	for line in f:
		line = line[:-1].split(' ')
		x = np.zeros(shape=(1, Dimension_Add_1))
		x = np.asmatrix(x)
		x.itemset((0, 0), 1)
		for i in range(2):
			x.itemset((0, i+1), float(line[i]))
		X[num] = x
		y[num] = [float(line[2])]
		num += 1
	f.close()

	I = np.identity(Dimension_Add_1)
	wReg = inv(Lambda * I + X.transpose() * X) * X.transpose() * y

	error = 0.0
	for i in range(size):
		if sign((wReg.transpose() * X[i].transpose()).item(0)) != y[i].item(0):
			error += 1

	print "Ein = " + str(error / float(size))

	f = open("hw4_test.dat", "r")
	X = np.zeros(shape=(test_size, Dimension_Add_1))
	y = np.zeros(shape=(test_size, 1))
	X = np.asmatrix(X)
	y = np.asmatrix(y)
	num = 0
	for line in f:
		line = line[:-1].split(' ')
		x = np.zeros(shape=(1, Dimension_Add_1))
		x = np.asmatrix(x)
		x.itemset((0, 0), 1)
		for i in range(2):
			x.itemset((0, i+1), float(line[i]))
		X[num] = x
		y[num] = [float(line[2])]
		num += 1
	f.close()

	error = 0.0
	for i in range(test_size):
		if sign((wReg.transpose() * X[i].transpose()).item(0)) != y[i].item(0):
			error += 1

	print "Eout = " + str(error / float(test_size))

if __name__ == '__main__':
	main()