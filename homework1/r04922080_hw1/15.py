def normalVectorCompute(a, b, s):
	ans = []
	for i in range(5):
		ans.append(a[i] + s*b[i])
	return ans

def innerProduct(a, b):
	ans = 0
	for i in range(5):
		ans += a[i]*b[i]
	return ans

def plusOrMinus(yn):
	if yn > 0 :
		return 1
	else :
		return -1

def main():
	f = open("hw1_15_train.dat", "r")
	data = []
	for line in f:
		line = line[:-1].split('\t');
		tmp = line[0].split(' ');
		member = []
		for i in tmp:
			member.append(float(i))
		member.append(float(1))
		member.append(float(line[1]))
		data.append(member)
	#print data
	f.close()

	w0 = [0, 0, 0, 0, 0]
	normalVector = data[0][:-1]

	# first normalVector update
	updateCount = 1
	lastErrorIndex = -1
	notYet = True
	while notYet == True :
		notYet = False
		for i in range(len(data)):
			vector = data[i]
			gn = innerProduct(normalVector, vector[:-1])
			gn = plusOrMinus(gn);

			if gn != vector[-1]:
				notYet = True
				updateCount += 1
				lastErrorIndex = i
				normalVector = normalVectorCompute(normalVector, vector[:-1], vector[-1])

	print "updates number : " + str(updateCount)
	print "last error index : " + str(lastErrorIndex)


if __name__ == '__main__':
	main();