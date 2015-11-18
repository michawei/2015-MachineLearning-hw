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

	Ein = []
	W_LIN_ALL = []
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
		# print W_LIN
		W_LIN_ALL.append(W_LIN)


	W_hat = np.zeros(shape=(6, 1))
	W_hat = np.asmatrix(W_hat)
	W3 = []
	for i in range(1000):
		W_hat += W_LIN_ALL[i]
		W3.append(W_LIN_ALL[i].item(3, 0))
	W_hat /= 1000.0
	
	# for i in range(6):
	# 	print float('%.6f' % W_hat.item(i))
	print float('%.6f' % W_hat.item(3))

	x = [-0.05, -0.04, -0.03 ,-0.02 ,-0.01, 0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11]
	y = [0 for i in range(16)]

	for num in W3:
		for i in range(16):
			if num >= x[i] and num < x[i+1]:
				y[i] += 1
				break

	plt.bar(x[:-1], y, width = 0.01 ,color = "#fad981")
	plt.title("14. w3 distribution")
	plt.xlabel("w3 value")
	plt.ylabel("times")
	plt.show()

	plt.plot(Ein)

if __name__ == '__main__':
	main()