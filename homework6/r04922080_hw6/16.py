import math
import numpy as np
import matplotlib.pyplot as plt

def sign(a):
	if ( a >= 0 ):
		return 1
	else:
		return -1

def decisionStump(s, x, theta):
	return s * sign(x - theta)

def main():

	f = open("hw2_adaboost_train.dat", "r")
	x_1 = [[0, 0]]
	x_2 = [[0, 0]]
	w = []
	G = []
	index = 0
	for line in f:
		line = line.strip().split()
		if line == '':
			break
		x_1.append([float(line[0]), float(line[2]), index])
		x_2.append([float(line[1]), float(line[2]), index])
		index += 1
	x_1.append([1, 0])
	x_2.append([1, 0])

	length = len(x_1)
	mother = float(length - 2)
	weight = 1.0 / mother
	for i in range(length - 2):
		w.append(weight)
		G.append(0.0)
	f.close()


	f = open("hw2_adaboost_test.dat", "r")
	x_1_test = []
	x_2_test = []
	for line in f:
		line = line.strip().split()
		if line == '':
			break
		x_1_test.append([float(line[0]), float(line[2])])
		x_2_test.append([float(line[1]), float(line[2])])
	f.close()

	x_1.sort()
	x_2.sort()

	Ein = []
	Ein_01 = []
	Epsilon = []
	for time in range(300):
		Ein_tmp = []
		for i in range(length - 1):
			# 1
			theta = (x_1[i][0] + x_1[i+1][0]) / 2.0
			s = 1.0
			error = 0.0
			for j in range(1, length - 1):
				if decisionStump(s, x_1[j][0], theta) != x_1[j][1]:
					error += w[x_1[j][2]]
			Ein_tmp.append([error, s, theta, 1])

			s = -1.0
			error = 0.0
			for j in range(1, length - 1):
				if decisionStump(s, x_1[j][0], theta) != x_1[j][1]:
					error += w[x_1[j][2]]
			Ein_tmp.append([error, s, theta, 1])

			# 2
			theta = (x_2[i][0] + x_2[i+1][0]) / 2.0
			s = 1.0
			error = 0.0
			for j in range(1, length - 1):
				if decisionStump(s, x_2[j][0], theta) != x_2[j][1]:
					error +=  w[x_2[j][2]]
			Ein_tmp.append([error, s, theta, 2])

			s = -1.0
			error = 0.0
			for j in range(1, length - 1):
				if decisionStump(s, x_2[j][0], theta) != x_2[j][1]:
					error +=  w[x_2[j][2]]
			Ein_tmp.append([error, s, theta, 2])

		Ein_tmp.sort()
		epsilon = Ein_tmp[0][0] / sum(w)
		diamond_t = math.sqrt(((1.0 - epsilon) / epsilon))
		error = 0.0
		if ( Ein_tmp[0][3] == 1 ):
			for j in range(1, length - 1):
				if decisionStump(Ein_tmp[0][1], x_1[j][0], Ein_tmp[0][2]) != x_1[j][1]:
					w[x_1[j][2]] *= diamond_t
					error += 1.0
				else:
					w[x_1[j][2]] /= diamond_t
		else:
			for j in range(1, length - 1):
				if decisionStump(Ein_tmp[0][1], x_2[j][0], Ein_tmp[0][2]) != x_2[j][1]:
					w[x_2[j][2]] *= diamond_t
					error += 1.0
				else:
					w[x_2[j][2]] /= diamond_t
		tmp = Ein_tmp[0]
		tmp.append(math.log(diamond_t))
		Ein.append(tmp)
		Ein_01.append(error/mother)

		Epsilon.append(epsilon)

	print "minimun epsilon = ", min(Epsilon)
	x = []
	for i in range(300):
		x.append(i)

	plt.plot(x, Epsilon)
	plt.title("16.")
	plt.xlabel("t")
	plt.ylabel("epsilon")
	plt.show()

if __name__ == '__main__':
	main()