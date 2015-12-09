from svmutil import *
import math
import numpy as np
import matplotlib.pyplot as plt

value = 8
C = [-6, -4, -2, 0, 2]

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

	alphas = []
	for c in C:
		prob  = svm_problem(y, x)
		param = svm_parameter('-t 1 -d 2 -c ' + str(math.pow(10, c)))
		m = svm_train(prob, param)

		y_alpha = np.array(m.get_sv_coef());
		
		alpha = 0
		for mem in y_alpha:
			alpha += abs(mem)
		print alpha
		alphas.append(alpha)
		# sv_matrix = []
		# for sv in svs:
		# 	sv_matrix.append([sv[1], sv[2]])

		# w = np.dot(np.transpose(y_alpha), sv_matrix)
		# norm_w = math.sqrt(math.pow(w[0][0], 2) + math.pow(w[0][1], 2))
		# print norm_w
		# W.append(norm_w)
	
	print alphas
	plt.plot(C, alphas)
	plt.title("17.")
	plt.xlabel("log(10)C")
	plt.ylabel("sigma(alpha)")
	plt.show()

if __name__ == '__main__':
	main()