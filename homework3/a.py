import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv


u = 0.0
v = 0.0

for _ in range(5):
    H = np.matrix([[np.exp(u) + math.pow(v, 2) * np.exp(u*v) + 2, np.exp(u*v) + u*v*np.exp(u*v) - 2], [np.exp(u*v) + u*v*np.exp(u*v) - 2, 4*np.exp(2*v) + math.pow(u, 2) * np.exp(u*v) + 4]])
    gradient_E = np.matrix([[np.exp(u) + v*np.exp(u*v) + 2*u - 2*v - 3],[2*np.exp(2*v) + u*np.exp(u*v) - 2*u + 4*v - 2]])

    print H
    print gradient_E
    print inv(H)
    gradient_ans = (-1) * inv(H) * gradient_E
    print gradient_ans
    u += gradient_ans.item(0, 0)
    v += gradient_ans.item(1, 0)
    print u
    print v
    print "-------------------------------"
# u = 0
# v = 0

# for _ in range(5):
#     U = np.exp(u) + v*np.exp(u*v) + 2*u - 2*v - 3
#     V = 2*np.exp(2*v) + u*np.exp(u*v) - 2*u + 4*v - 2

#     print U
#     print V
#     u = u - 0.01 * U
#     v = v - 0.01 * V
# print u, v

print u
print v

E = np.exp(u) + np.exp(2*v) + np.exp(u*v) + math.pow(u, 2) - 2*u*v + 2*math.pow(v, 2) - 3*u - 2*v
print "Ans: ", E