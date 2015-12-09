from svmutil import *
import math
import numpy as np
import matplotlib.pyplot as plt

value = 0
C = [-3, -2, -1, 0, 1]

def main():

	f = open("features.train", "r")
	y = []
	x = []
	for line in f:
		line = line.strip().split()
		if line == '':
			break
		if float(line[0]) == value:
			ans = 1
		else:
			ans = -1
		tmp = []
		tmp.append(float(line[1]))
		tmp.append(float(line[2]))
		y.append(ans)
		x.append(tmp)
	f.close()

	f = open("features.test", "r")
	y_test = []
	x_test = []
	for line in f:
		line = line.strip().split()
		if line == '':
			break
		if float(line[0]) == value:
			ans = 1
		else:
			ans = -1
		tmp = []
		tmp.append(float(line[1]))
		tmp.append(float(line[2]))
		y_test.append(ans)
		x_test.append(tmp)
	f.close()

	distance = []
	for c in C:
		print "---------------------" + str(c) + "------------------------"
		prob  = svm_problem(y, x)
		param = svm_parameter('-t 2 -g 100 -c ' + str(math.pow(10, c)))
		m = svm_train(prob, param)


	####################### This ||w|| is from traning #######################
	# w = [ 0.121384, 1.212441, 7.761528, 11.882027, 24.329622 ]

	# for i in range(len(w)):
	# 	w[i] = 1.0 / w[i]
	# print w

	# plt.plot(C, w)
	# plt.title("18.")
	# plt.xlabel("log(10)C")
	# plt.ylabel("distance")
	# plt.show()

if __name__ == '__main__':
	main()