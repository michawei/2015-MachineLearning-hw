import math
import matplotlib.pyplot as plt

N = 10000.0
d = 50.0
g = 0.05

# a = float(2 * N - 4.0)
# b = float(-4.0)
# c = float(-(math.log(4.0) + 2 * d * math.log(N) - math.log(g) ))

# a = float(N)
# b = float(-2.0)
# c = float(-math.log(6.0 * math.pow(2*N, d) / g))
x = []
y = []
for i in range(1, 10001):
    N = i
    x.append(N)
    # a = float(2 * N - 4.0)
    # b = float(-4.0)
    # c = float(-(math.log(4.0) + 2 * d * math.log(N) - math.log(g) ))
    a = float(N)
    b = float(-2.0)
    c = float(-math.log(6.0 * math.pow(2*N, d) / g))
    if a != 0:
        delta = b ** 2 - 4 * a * c;
        if delta < 0:
            print 'No solution', N
            y.append(0)
        elif delta == 0:
            s = -b / (2 * a);
            print 'Solution is', s
            y.append(s)
        else:
            root = math.sqrt(delta)
            s1 = (-b + root) / (2 * a)
            s2 = (-b - root) / (2 * a)
            print 'Solutions are', s1, s2
            y.append(s1)
    else:
        print c/b
        y.append(c/b)

plt.title("Parrondo and Van den Broek")
plt.xlabel("N")
plt.ylabel("epsilon")
plt.plot(x, y, linewidth = 3)
plt.show()

# i = (2.0 / N) * math.log(2.0 * N * math.pow(N, d))
# ans = math.sqrt(i)
# ans += math.sqrt((2.0 / N) * math.log(1 / g)) + (1 / N)
# print ans

# i = (16.0 / N) * math.log(2.0 * math.pow(N, d) / math.sqrt(g))
# ans = math.sqrt(i)
# print ans

# i = (8 / N) * math.log(4.0 * math.pow(2*N, d) / g)
# ans = math.sqrt(i)
# print ans