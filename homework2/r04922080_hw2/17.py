import numpy as np
import random
import matplotlib.pyplot as plt

def sign(a):
	if a >= 0:
		return 1
	else:
		return -1

def main():

	Ein = []

	for times in range(5000):
		data = []
		ans = []
		#data.append(-1.0)
		for i in range(20):
			x = np.random.uniform(-1, 1)
			data.append(x)
		data.sort()
		#print data

		for x in data:
			if sign(x) == 1:
				r = random.random()
				if r <= 0.2:
					ans.append(-1)
				else:
					ans.append(1)
			else:
				r = random.random()
				if r <= 0.2:
					ans.append(1)
				else:
					ans.append(-1)

		thetas = []
		thetas.append((-1.0 + data[0]) / 2)
		for i in range(0, 19):
			thetas.append((data[i]+data[i+1])/2)
		thetas.append((data[19] + 1.0) / 2)
		#print thetas

		Einmin = 2
		for theta in thetas:
			s = 1
			error = 0.0
			for i in range(len(data)):
				if s * sign( data[i] - theta ) != ans[i]:
					error += 1
			e = error / 20.0
			#print e
			if e < Einmin:
				Einmin = e

			s = -1
			error = 0.0
			for i in range(len(data)):
				if s * sign( data[i] - theta ) != ans[i]:
					error += 1
			e = error / 20.0
			#print e
			if e < Einmin:
				Einmin = e
		#print Einmin
		Ein.append(Einmin)
	print "average Ein = " + str(sum(Ein) / float(len(Ein)))

	x = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.0]
	y = [0 for i in range(20)]

	for num in Ein:
		for i in range(20):
			if num >= x[i] and num < x[i+1]:
				y[i] += 1
				break

	plt.bar(x[:-1], y, width = 0.05 ,color = "#fad981")
	plt.title("17. Ein distribution")
	plt.xlabel("Error Rate")
	plt.ylabel("times")
	plt.show()

	plt.plot(Ein)

if __name__ == '__main__':
	main()