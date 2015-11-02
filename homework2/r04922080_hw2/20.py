
theta = 1.6175
s = -1

def sign(a):
	if a >= 0:
		return 1
	else:
		return -1

def main():
	f = open("hw2_test.dat", "r")
	test_data = []

	for line in f:
		line = line[1:-1].split(' ')
		#print line
		test_data.append([float(line[3]), int(line[9])])
	
	error = 0.0
	length = len(test_data)
	for j in range(length):
		x = test_data[j]
		if s * sign( x[0] - theta ) != x[1]:
			error += 1

	Eout = error / float(length)
	print "Eout = ", Eout
	#print sum(Etest)/float(len(Etest))


if __name__ == '__main__':
	main()