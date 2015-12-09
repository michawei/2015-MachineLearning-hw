from svmutil import *
import math
import numpy as np
import matplotlib.pyplot as plt
import random

value = 0
C = 0.1
gamma = [0, 1, 2, 3, 4]

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
	length = len(y)

	gamma_num = [0, 0, 0, 0, 0]

	for time in range(100):
		print "--------------------" + str(time) + "--------------------------"
		index = random.sample(range(length), 1000)

		y_train = []
		x_train = []
		y_val = []
		x_val = []
		for i in range(length):
			if i in index:
				y_val.append(y[i])
				x_val.append(x[i])
			else:
				y_train.append(y[i])
				x_train.append(x[i])

		Eval = []
		for g in gamma:
			prob  = svm_problem(y_train, x_train)
			param = svm_parameter('-t 2 -g ' + str(math.pow(10, g)) + ' -c ' + str(C))
			m = svm_train(prob, param)
			p_label, p_acc, p_val = svm_predict(y_val, x_val, m)
			
			acc = p_acc[0]
			Eval_tmp = (100 - acc)/100.0
			Eval.append([Eval_tmp, g])

		min_gamma = -1
		min_Eval = 2147483647
		for mem in Eval:
			if mem[0] < min_Eval:
				min_Eval = mem[0]
				min_gamma = mem[1]
		gamma_num[min_gamma] += 1
		
	print gamma_num
	plt.bar(gamma, gamma_num, width = 1 ,color = "#fad981")
	plt.title("20.")
	plt.xlabel("log(10)gamma")
	plt.ylabel("times")
	plt.show()

if __name__ == '__main__':
	main()