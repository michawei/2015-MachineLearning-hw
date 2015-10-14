import random
import matplotlib.pyplot as plt

def normalVectorCompute(a, b, s):
	ans = []
	for i in range(5):
		ans.append(a[i] + float(0.5)*s*b[i])
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

	twoThousantUpdate = []
	for count in range(2000):

		indexRandom = range(len(data))
		random.shuffle(indexRandom)

		normalVector = data[indexRandom[0]][:-1]

		# first normalVector update
		updateCount = 1
		notYet = True
		while notYet == True :
			notYet = False
			for i in indexRandom:
				vector = data[i]
				gn = innerProduct(normalVector, vector[:-1])
				gn = plusOrMinus(gn);

				if gn != vector[-1]:
					notYet = True
					updateCount += 1
					normalVector = normalVectorCompute(normalVector, vector[:-1], vector[-1])
		twoThousantUpdate.append(updateCount);

	x = range(max(twoThousantUpdate)+1)
	y = [0 for i in range(max(twoThousantUpdate)+1)]

	ans = float(0)
	for num in twoThousantUpdate:
		ans += num
		y[num] += 1
	
	print "average updates = " + str(ans/float(len(twoThousantUpdate)))
	plt.bar(x, y, color = "#20b2aa")
	plt.title("17. Number of Updates versus Frequency ( Eta = 0.5 )")
	plt.xlabel("Updates")
	plt.ylabel("Frequency")
	plt.show()

if __name__ == '__main__':
	main();