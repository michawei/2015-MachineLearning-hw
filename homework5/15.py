from svmutil import *
import math

value = 0
C = [0.000001, 0.0001, 0.001, 1, 100]

def main():

	f = open("features.train", "r")
	y = []
	x = []
	for line in f:
		line = line[:-1].split(' ')
		if line[0] == value:
			ans = 1
		else:
			ans = -1
		tmp = []
		print line[1]
		tmp.append(float(line[1]))
		tmp.append(float(line[2]))
		y.append(ans)
		x.append(tmp)
	f.close()

	f = open("features.test", "r")
	y_test = []
	x_test = []
	for line in f:
		line = line[:-1].split(' ')
		if line[0] == value:
			ans = 1
		else:
			ans = -1
		tmp = []
		tmp.append(float(line[1]))
		tmp.append(float(line[2]))
		y_test.append(ans)
		x_test.append(tmp)
	f.close()

	for c in C:
		prob  = svm_problem(y, x)
		param = svm_parameter('-t 0 -c ' + str(c))
		m = svm_train(prob, param)
		p_label, p_acc, p_val = svm_predict(y_test, x_test, m)
		print p_label
		print p_acc
		print p_val
		break

if __name__ == '__main__':
	main()