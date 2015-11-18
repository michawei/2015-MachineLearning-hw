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
	for times in range(1000):
		# data = []
		X = np.zeros(shape=(1000, 3))
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
			X[i] = [1, x1, x2]
			y[i] = [ans]
			# data.append([x1, x2, ans])

		W_LIN = inv(X.transpose()*X)*X.transpose()*y
		y_hat = X*W_LIN

		#print y_hat
		error = 0
		for i in range(1000):
			if sign(y_hat.item(i)) != y[i]:
				error += 1
		Ein.append(error / 1000.0)
	print sum(Ein) / float(len(Ein))

	x = [0.35, 0.36, 0.37, 0.38, 0.39, 0.40, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66]
	y = [0 for i in range(31)]

	for num in Ein:
		for i in range(31):
			if num >= x[i] and num < x[i+1]:
				y[i] += 1
				break

	plt.bar(x[:-1], y, width = 0.01 ,color = "#fad981")
	plt.title("13. Ein distribution")
	plt.xlabel("Error in")
	plt.ylabel("times")
	plt.show()

	# plt.plot(Ein)

if __name__ == '__main__':
	main()