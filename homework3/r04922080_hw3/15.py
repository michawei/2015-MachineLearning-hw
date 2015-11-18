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

	Eout = []
	for times in range(1000):
		# data = []
		X = np.zeros(shape=(1000, 6))
		y = np.zeros(shape=(1000, 1))
		X = np.asmatrix(X)
		y = np.asmatrix(y)
		for i in range(1000):
			x1 = np.random.uniform(-1, 1)
			x2 = np.random.uniform(-1, 1)
			ans = sign(math.pow(x1, 2) + math.pow(x2, 2) - 0.6)

			r = random.random()
			if r <= 0.1:
				ans *= -1
			
			X[i] = [1, x1, x2, x1*x2, math.pow(x1, 2), math.pow(x2, 2)]
			y[i] = [ans]
			# data.append([x1, x2, ans])

		W_LIN = inv(X.transpose()*X)*X.transpose()*y

		error = 0.0
		for i in range(1000):
			x = np.zeros(shape=(1, 6))
			x = np.asmatrix(x)
			x1 = np.random.uniform(-1, 1)
			x2 = np.random.uniform(-1, 1)
			ans = sign(math.pow(x1, 2) + math.pow(x2, 2) - 0.6)

			r = random.random()
			if r <= 0.1:
				ans *= -1
			
			x = [1, x1, x2, x1*x2, math.pow(x1, 2), math.pow(x2, 2)]
			if ans != sign(x * W_LIN):
				error += 1
		Eout.append(error/1000.0)

	#print Eout
	print sum(Eout) / float(len(Eout))

	x = [0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21]
	y = [0 for i in range(16)]

	for num in Eout:
		for i in range(16):
			if num >= x[i] and num < x[i+1]:
				y[i] += 1
				break

	plt.bar(x[:-1], y, width = 0.01 ,color = "#fad981")
	plt.title("15. Eout distribution")
	plt.xlabel("Error out rate")
	plt.ylabel("times")
	plt.show()

if __name__ == '__main__':
	main()