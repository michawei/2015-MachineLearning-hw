import numpy as np
import random
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv

def sign(a):
	if a >= 0:
		return 1
	else:
		return -1

def main():

	f = open("hw3_train.dat", "r")
	#train_data = []
	X = np.zeros(shape=(1000, 21))
	y = np.zeros(shape=(1000, 1))
	X = np.asmatrix(X)
	y = np.asmatrix(y)
	num = 0
	for line in f:
		line = line[1:-1].split(' ')
		#print line
		x = np.zeros(shape=(1, 21))
		x = np.asmatrix(x)
		x.itemset((0, 0), 1)
		for i in range(20):
			x.itemset((0, i+1), float(line[i]))
		X[num] = x
		y[num] = [float(line[20])]
		#train_data.append(line)
		num += 1
	f.close()

	# print X
	W_t = np.zeros(shape=(21, 1))
	W_t = np.asmatrix(W_t)
	Eta = 0.001

	for _ in range(2000):
		gradient_E = np.zeros(shape=(21, 1))
		gradient_E = np.asmatrix(gradient_E)
		for i in range(1000):
			gradient_E += (1.0 / (1 + np.exp( y.item(i) * (X[i]*W_t).item(0) ) )) * (-1) * y.item(i) * X[i].transpose()
		gradient_E /= 1000.0
		W_t -= Eta * gradient_E
	print W_t

	f = open("hw3_test.dat", "r")
	Eout = 0.0
	for line in f:
		line = line[1:-1].split(' ')
		#print line
		x = np.zeros(shape=(1, 21))
		x = np.asmatrix(x)
		x.itemset((0, 0), 1)
		for i in range(20):
			x.itemset((0, i+1), float(line[i]))
		out = 1.0/(1+np.exp((-1)*(x*W_t).item(0)))
		if out <= 0.5:
			out = -1
		else:
			out = 1
		if out != int(line[20]):
			Eout += 1
		# Eout += math.log(1 + np.exp( (-1) * float(line[20]) * (x*W_t).item(0) ))
		# if sign((x * W_t).item(0)) != float(line[20]):
		# 	error += 1.0
	f.close()
	print Eout / 3000.0


if __name__ == '__main__':
	main()