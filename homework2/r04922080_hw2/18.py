import numpy as np
import random
import matplotlib.pyplot as plt

def sign(a):
	if a >= 0:
		return 1
	else:
		return -1

def main():

	Eout = []
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
		choose_theta = 0
		choose_s = 0
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
				choose_theta = theta
				choose_s = s

			s = -1
			error = 0.0
			for i in range(len(data)):
				if s * sign( data[i] - theta ) != ans[i]:
					error += 1
			e = error / 20.0
			#print e
			if e < Einmin:
				Einmin = e
				choose_theta = theta
				choose_s = s
		Eout.append( 0.5 + 0.3 * choose_s * (abs(choose_theta) - 1) )

	print "average Eout = " + str(sum(Eout)/float(len(Eout)))

	x = [0.100, 0.125, 0.150, 0.175, 0.200, 0.225, 0.250, 0.275, 0.300, 0.325, 0.350, 0.375, 0.400, 0.425, 0.450, 0.475, 0.500, 0.525, 0.550, 0.575, 1.0]
	y = [0 for i in range(20)]

	for num in Eout:
		for i in range(20):
			if num >= x[i] and num < x[i+1]:
				y[i] += 1
				break

	plt.bar(x[:-1], y, width = 0.025, color = "#fad981")
	plt.title("18. Eout distribution")
	plt.xlabel("Error Rate")
	plt.ylabel("times")
	plt.show()

	plt.plot(Eout)

if __name__ == '__main__':
	main()