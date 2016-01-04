import math
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

Gamma = [32, 2, 0.125]
Lambda = [0.001, 1, 1000]
size = 400

def sign(a):
	if ( a >= 0 ):
		return 1
	else:
		return -1

def main():

	f = open("hw2_lssvm_all.dat", "r")
	x = []
	y = []
	x_test = []
	y_test = []
	num = 0
	for line in f:
		line = line.strip().split()
		if line == '':
			break
		tmp = []
		for string in line[:-1]:
			tmp.append(float(string))
		x.append(tmp)
		y.append(float(line[-1]))
		num += 1
		if num == size:
			break

	x = np.asmatrix(x)
	y = np.asmatrix(y)

	for line in f:
		line = line.strip().split()
		if line == '':
			break
		tmp = []
		for string in line[:-1]:
			tmp.append(float(string))
		x_test.append(tmp)
		y_test.append(float(line[-1]))

	length = len(x)
	Ein = []
	for gamma in Gamma:
		# K
		K = np.zeros(shape=(size, size))
		K = np.asmatrix(K)
		for i in range(size):
			for j in range(size):
				tmp = x[i] - x[j]
				L = math.exp((tmp*tmp.transpose()).item(0) * (-1) * gamma)
				K.itemset((i, j), L)

		for lambdaa in Lambda:
			Beta = inv(lambdaa * np.identity(size) + K) * y.transpose()
			error = 0.0
			for i in range(length):
				g = 0.0
				for j in range(length):
					g += Beta.item(j) * K.item((j, i))
				if y.item(i) != sign(g):
					error += 1.0
			error /= float(length)
			Ein.append([error, gamma, lambdaa])
	Ein.sort()
	for mem in Ein:
		if mem[0] == 0:
			print "min Ein = ", mem[0], ", gamma = ", mem[1], ", lambda = ", mem[2]

if __name__ == '__main__':
	main()