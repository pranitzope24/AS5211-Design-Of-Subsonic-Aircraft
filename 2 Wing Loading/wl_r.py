#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import math

### CONSTANTS
F_1 = 0.01203321162
F_2 = 0.000002307238425
k = 0.04356653045
V_c = 12.7*np.sqrt(0.3218995598)
rho = 1.225
a=[-0.00139829, 0.76439155]
x = np.linspace(3000, 12000, 12000)
y = []

### Thrust vs Wing loading function, all constants listed above
def fun1(p):
    ans = 1264.61074551*(0.01203321162/p+2.307*10**(-6)+4.187*10**(-10) *p)
    return ans

### Finds minimum value of x where the minimum lies
min_y = 1000000000000
min_x = 0
for i in range(0,len(x)):
    y.append(fun1(x[i]))
    curr = fun1(x[i])
    if(min_y>curr):
        min_y = curr
        min_x = x[i]

print (min_x)

y_new = min_y
y_new += min_y*0.05   ### 5% error (only parabolic curves)

print(y_new)

x_pl = [3640.06, 7891.64]  #see from graph and change the P min and P max value here
y_pl = [fun1(3640.06), fun1(7891.64)]

### PLOT
plt.figure()
plt.grid(linestyle='--')
plt.title("Plot for Range")
plt.xlabel("P")
plt.ylabel("$W_f/W_{mean}$")
plt.plot(x, fun1(x), '-')
plt.plot(min_x, min_y, 'o', label="Minimum Value")
plt.plot(x_pl,y_pl, 'o', label="5 percent Thershold")
plt.plot(x,y_new*np.ones(len(x)),'g--' ,label = "5 percent Threshold", linewidth = 0.85)
plt.legend()
plt.show()
plt.close()
