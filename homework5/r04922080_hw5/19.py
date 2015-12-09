from svmutil import *
import math
import numpy as np
import matplotlib.pyplot as plt

value = 0
C = 0.1
gamma = [0,1,2,3,4]

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

	Eout = []
	for g in gamma:
		prob  = svm_problem(y, x)
		param = svm_parameter('-t 2 -g ' + str(math.pow(10, g)) + ' -c ' + str(C))
		m = svm_train(prob, param)
		p_label, p_acc, p_val = svm_predict(y_test, x_test, m)
		
		acc = p_acc[0]
		Eout_tmp = (100 - acc)/100.0
		Eout.append(Eout_tmp)

	print Eout
	plt.plot(gamma, Eout)
	plt.title("19.")
	plt.xlabel("log(10)gamma")
	plt.ylabel("Eout")
	plt.show()

if __name__ == '__main__':
	main()