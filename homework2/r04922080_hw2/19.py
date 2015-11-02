def sign(a):
	if a >= 0:
		return 1
	else:
		return -1

def main():
	f = open("hw2_train.dat", "r")
	train_data = []
	for i in range(9):
		train_data.append([])

	for line in f:
		line = line[1:-1].split(' ')
		#print line
		for i in range(9):
			train_data[i].append([float(line[i]), int(line[9])])
	

	Ein = []
	for i in range(9):
		train_data[i].sort()
		thetas = []
		data_size = len(train_data[i])
		for j in range(data_size-1):
			thetas.append( ( train_data[i][j][0] + train_data[i][j+1][0])/2 )

		Einmin = 2
		choose_theta = 0
		choose_s = 0
		d = -1
		for theta in thetas:
			s = 1
			error = 0.0
			for x in train_data[i]:
				if s * sign( x[0] - theta ) != x[1]:
					error += 1
			e = error / float(data_size)
			#print e
			if e < Einmin:
				Einmin = e
				choose_theta = theta
				choose_s = s
				d = i

			s = -1
			error = 0.0
			for x in train_data[i]:
				if s * sign( x[0] - theta ) != x[1]:
					error += 1
			e = error / float(data_size)
			#print e
			if e < Einmin:
				Einmin = e
				choose_theta = theta
				choose_s = s
				d = i
		Ein.append([Einmin, choose_theta, choose_s, d])

	Ein.sort()
	#print Ein[0][3]
	print "Ein of the optimal decision stump = " + str(Ein[0][0])
	print "the optimal decision stump, theta = " + str(Ein[0][1]) + ", s = " + str(Ein[0][2])

if __name__ == '__main__':
	main()