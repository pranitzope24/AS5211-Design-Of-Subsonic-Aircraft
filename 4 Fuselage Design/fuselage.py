import numpy as np
import matplotlib.pyplot as plt
import math




l = [
    # 12.77,
    20,
    # 13.7,
    22.63,
    28.6,
    # 13.26,
    40.59,
    29.79,
    36.24,
    # 7.8,
    # 8.8
    35.1,
	32.86
]
mtow = [
    # 4580,
    11500,
    # 7938,
    19278,
    44225,
    # 11860,
    95100,
    70307,
    61500,
    # 1996
    # 3130
    70900,
    70760
]

w = [
    # 15.32,
    19.78,
    # 13.65,
    27.97,
    26.34,
    # 22.12,
    32.92,
    40.41,
    33.72,
    # 11.81,
    # 13.51,
    35.1,
    32.86
]


ll = []
lm = []
lb = []

for i in range(0, len(l)):
    ll.append(math.log(l[i]))
    lm.append(math.log(mtow[i]))
    lb.append(math.log(w[i]))

m, c = np.polyfit(lm, ll, 1)
A = math.e ** c
L = m   
print(A, L)

x_axis = np.linspace(min(lm), max(lm), 50)
y_axis = m*x_axis + c

plt.figure()
plt.grid(linestyle='--')
plt.title("Logarithmic scale plot for MTOW vs L")
plt.ylabel("log($L$)")
plt.xlabel("log($MTOW$)")
plt.plot(lm, ll, '.', label='Scatter Plot')
plt.plot(x_axis, y_axis, label='Linear Best Fit Line')
plt.legend()
plt.show()
plt.close()


x_axis = np.linspace(min(mtow), max(mtow), 50)
y_axis = A*x_axis**L

k = A*57236.016**L
print (k)

plt.figure()
plt.grid(linestyle='--')
plt.title("Plot for L vs MTOW ")
plt.ylabel("$L$")
plt.xlabel("$MTOW$")
plt.plot(mtow, l,'.', label='Scatter Plot')
plt.plot(x_axis, y_axis, label='Best Fit Curve')
plt.plot(57236.016,k,'g*', label = 'Optimal Point')
plt.legend()
plt.show()
plt.close()







m, c = np.polyfit(lb, ll, 1)
A = math.e ** c
L = m   
print(A, L)

x_axis = np.linspace(min(lb), max(lb), 50)
y_axis = m*x_axis + c

plt.figure()
plt.grid(linestyle='--')
plt.title("Logarithmic scale plot for b vs L")
plt.ylabel("log($L$)")
plt.xlabel("log($b$)")
plt.plot(lb, ll, '.', label='Scatter Plot')
plt.plot(x_axis, y_axis, label='Linear Best Fit Line')
plt.legend()
plt.show()
plt.close()


x_axis = np.linspace(min(w), max(w), 50)
y_axis = A*x_axis**L

k = A*30.276**L
print (k)

plt.figure()
plt.grid(linestyle='--')
plt.title("Plot for L vs b ")
plt.ylabel("$L$")
plt.xlabel("$b$")
plt.plot(w, l,'.', label='Scatter Plot')
plt.plot(x_axis, y_axis, label='Best Fit Curve')
plt.plot(30.276,k,'g*', label = 'Optimal Point')
plt.legend()
plt.show()
plt.close()