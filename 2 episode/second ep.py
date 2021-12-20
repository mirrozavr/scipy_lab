import numpy as np
import matplotlib.pyplot as plt

f = open('large.txt', 'r')
k = 0
while True:
    line = f.readline()
    if not line:
        break
    if len(line.split()) == 1:
        N = int(line.split()[0])
        a = np.zeros((N, N))
        b = np.zeros((N,))
    if (k < N) and (len(line.split()) == N):
        m = 0
        while m != N:
            for i in line.split():
                a[k][m] = float(i)
                m += 1
        k += 1
    elif (k >= N):
        m = 0
        while m != N:
            for i in line.split():
                b[m] = float(i)
                m += 1

objects = np.arange(1,N+1)
performance = np.linalg.solve(a, b)

fig, ax = plt.subplots()
ax.grid()
ax.bar(objects, performance, color='violet')
plt.savefig('res_large.png')
plt.show()