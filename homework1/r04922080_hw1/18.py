import random
import matplotlib.pyplot as plt

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

def checkErrorRate(w, testData, size):
	error = 0
	for member in testData:
		gn = innerProduct(w, member)
		gn = plusOrMinus(gn)
		if gn != member[-1]:
			error += 1
	return float(error)/size

def main():
	f = open("hw1_18_train.dat", "r")
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

	f = open("hw1_18_test.dat", "r")
	testData = []
	for line in f:
		line = line[:-1].split('\t');
		tmp = line[0].split(' ');
		member = []
		for i in tmp:
			member.append(float(i))
		member.append(float(1))
		member.append(float(line[1]))
		testData.append(member)
	#print testData
	f.close()
	sizeOfTestData = float(len(testData))

	twoThousantErrorRate = []
	for count in range(2000):

		#print count
		
		indexRandom = range(len(data))
		random.shuffle(indexRandom)

		normalVector = data[indexRandom[0]][:-1]

		# first normalVector update
		updateCount = 1
		pocket = []
		pocketErrorRate = float(1)
		#notYet = True
		while updateCount != 50 :
			#notYet = False
			for i in indexRandom:
				vector = data[i]
				gn = innerProduct(normalVector, vector[:-1])
				gn = plusOrMinus(gn);

				if gn != vector[-1]:
					#notYet = True
					updateCount += 1
					normalVector = normalVectorCompute(normalVector, vector[:-1], vector[-1])
					errorRate = checkErrorRate(normalVector, data, sizeOfTestData)

					if errorRate < pocketErrorRate:
						pocketErrorRate = errorRate
						pocket = normalVector

					if updateCount == 50:
						break
		pocketErrorRate = checkErrorRate(pocket, testData, sizeOfTestData)
		twoThousantErrorRate.append(pocketErrorRate)
		
	#print twoThousantErrorRate
	x = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30]
	y = [0 for i in range(30)]

	ans = float(0)
	for num in twoThousantErrorRate:
		ans += num
		for i in range(30):
			if num > x[i] and num < x[i+1]:
				y[i] += 1
				break
	#print pocket
	#print x
	#print y

	print "average Error Rate = " + str(ans/float(len(twoThousantErrorRate)))

	#plt.hist(twoThousantErrorRate)
	plt.bar(x[:-1], y, width = 0.01 ,color = "#fad981")
	plt.title("18. Error Rate versus Frequency ( pocket, 50 updates ) ")
	plt.xlabel("Error Rate")
	plt.ylabel("Frequency")
	plt.show()

if __name__ == '__main__':
	main();