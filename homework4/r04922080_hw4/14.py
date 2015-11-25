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

	f = open("hw4_test.dat", "r")
	X_test = np.zeros(shape=(test_size, Dimension_Add_1))
	y_test = np.zeros(shape=(test_size, 1))
	X_test = np.asmatrix(X_test)
	y_test = np.asmatrix(y_test)
	num = 0
	for line in f:
		line = line[:-1].split(' ')
		x = np.zeros(shape=(1, Dimension_Add_1))
		x = np.asmatrix(x)
		x.itemset((0, 0), 1)
		for i in range(2):
			x.itemset((0, i+1), float(line[i]))
		X_test[num] = x
		y_test[num] = [float(line[2])]
		num += 1
	f.close()

	Ein = []
	plot_x = []
	plot_y = []
	for i in range(-10, 3):
		power = - 8 - i
		Lambda = math.pow(10, power)
		I = np.identity(Dimension_Add_1)
		wReg = inv(Lambda * I + X.transpose() * X) * X.transpose() * y

		error = 0.0
		for j in range(size):
			if sign((wReg.transpose() * X[j].transpose()).item(0)) != y[j].item(0):
				error += 1
		ein = error / float(size)
		Ein.append([ein, power, wReg])
		plot_x.append(power)
		plot_y.append(ein)

	minimum = Ein[0][0]
	for member in Ein:
		if minimum > member[0]:
			minimum = member[0]
			ans = member

	print "When log10(lambda) = " + str(ans[1]) + ", we have minimum Ein."
	print "Ein = " + str(ans[0])
	wReg = ans[2]

	error = 0.0
	for i in range(test_size):
		if sign((wReg.transpose() * X_test[i].transpose()).item(0)) != y_test[i].item(0):
			error += 1

	print "Eout = " + str(error / float(test_size))


	plt.bar(plot_x, plot_y, width = 1 ,color = "#fad981")
	plt.title("14. Curve of Ein with respect to log10(lambda)")
	plt.xlabel("log10(lambda)")
	plt.ylabel("Ein")
	plt.show()

if __name__ == '__main__':
	main()