import numpy as np
import random
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv

Lambda = 11.26
train_size = 160
val_size = 40
Dimension_Add_1 = 3
test_size = 1000

def sign(a):
	if a >= 0:
		return 1
	else:
		return -1

def main():

	X = []
	y = []
	X_fold = []
	y_fold = []
	for fold in range(5):
		X_train = np.zeros(shape=(train_size, Dimension_Add_1))
		y_train = np.zeros(shape=(train_size, 1))
		X_train = np.asmatrix(X_train)
		y_train = np.asmatrix(y_train)

		X_val = np.zeros(shape=(val_size, Dimension_Add_1))
		y_val = np.zeros(shape=(val_size, 1))
		X_val = np.asmatrix(X_val)
		y_val = np.asmatrix(y_val)
		f = open("hw4_train.dat", "r")
		cut_first = fold * 40
		cut_second = (fold+1) * 40

		num = 0
		if fold != 0:
			for line in f:
				line = line[:-1].split(' ')
				x = np.zeros(shape=(1, Dimension_Add_1))
				x = np.asmatrix(x)
				x.itemset((0, 0), 1)
				for i in range(2):
					x.itemset((0, i+1), float(line[i]))
				X_train[num] = x
				y_train[num] = [float(line[2])]
				num += 1
				if num == cut_first:
					break

		num = 0
		for line in f:
			line = line[:-1].split(' ')
			x = np.zeros(shape=(1, Dimension_Add_1))
			x = np.asmatrix(x)
			x.itemset((0, 0), 1)
			for i in range(2):
				x.itemset((0, i+1), float(line[i]))
			X_val[num] = x
			y_val[num] = [float(line[2])]
			num += 1
			if num == 40:
				break

		num = 0
		if fold != 4:
			for line in f:
				line = line[:-1].split(' ')
				x = np.zeros(shape=(1, Dimension_Add_1))
				x = np.asmatrix(x)
				x.itemset((0, 0), 1)
				for i in range(2):
					x.itemset((0, i+1), float(line[i]))
				X_train[num+cut_first] = x
				y_train[num+cut_first] = [float(line[2])]
				num += 1
		f.close()
		X.append(X_train)
		y.append(y_train)
		X_fold.append(X_val)
		y_fold.append(y_val)
		# print X_train
		# print X_val

	# f = open("hw4_test.dat", "r")
	# X_test = np.zeros(shape=(test_size, Dimension_Add_1))
	# y_test = np.zeros(shape=(test_size, 1))
	# X_test = np.asmatrix(X_test)
	# y_test = np.asmatrix(y_test)
	# num = 0
	# for line in f:
	# 	line = line[:-1].split(' ')
	# 	x = np.zeros(shape=(1, Dimension_Add_1))
	# 	x = np.asmatrix(x)
	# 	x.itemset((0, 0), 1)
	# 	for i in range(2):
	# 		x.itemset((0, i+1), float(line[i]))
	# 	X_test[num] = x
	# 	y_test[num] = [float(line[2])]
	# 	num += 1
	# f.close()

	Ecv = []
	plot_x = []
	plot_y = []
	for i in range(-10, 3):
		power = - 8 - i
		Lambda = math.pow(10, power)
		I = np.identity(Dimension_Add_1)

		E = []
		for fold in range(5):
			X_train = X[fold]
			y_train = y[fold]
			X_val = X_fold[fold]
			y_val = y_fold[fold]
			# print X_train
			# print X_val
			wReg = inv(Lambda * I + X_train.transpose() * X_train) * X_train.transpose() * y_train

			error = 0.0
			for j in range(val_size):
				if sign((wReg.transpose() * X_val[j].transpose()).item(0)) != y_val[j].item(0):
					error += 1
			e = error / float(val_size)
			E.append(e)
		# print E
		mean = sum(E) / float(len(E))
		Ecv.append([mean, power])
		plot_x.append(power)
		plot_y.append(mean)

	minimum = Ecv[0][0]
	for member in Ecv:
		if minimum > member[0]:
			minimum = member[0]
			ans = member

	print "When log10(lambda) = " + str(ans[1]) + ", we have minimum Ecv."
	print "Ecv = " + str(ans[0])

	# error = 0.0
	# for i in range(train_size):
	# 	if sign((wReg.transpose() * X_train[i].transpose()).item(0)) != y_train[i].item(0):
	# 		error += 1

	# print "Etrain = " + str(error / float(train_size))
	# print "Eval = " + str(ans[0])

	# error = 0.0
	# for i in range(test_size):
	# 	if sign((wReg.transpose() * X_test[i].transpose()).item(0)) != y_test[i].item(0):
	# 		error += 1

	# print "Eout = " + str(error / float(test_size))

	plt.bar(plot_x, plot_y, width = 1 ,color = "#fad981")
	plt.title("19. Ecv with respect to log10(lambda)")
	plt.xlabel("log10(lambda)")
	plt.ylabel("Ecv")
	plt.show()

if __name__ == '__main__':
	main()