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
def fun1(x):
    y=x/2.632908425
    return y

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

y_new1 = 1800
y_new1 += 1800*0.1  ### 5% error (only parabolic curves)
y_new2 = 1800 - 1800*0.1

print(y_new1, y_new2)

x_pl = [4263.52, 5212.26]  #see from graph and change the P min and P max value here
y_pl = [fun1(4263.52), fun1(5212.26)]

### PLOT
plt.figure()
plt.grid(linestyle='--')
plt.title("Plot for Landing Distance")
plt.xlabel("P")
plt.plot(x, fun1(x), '-')
plt.plot(x_pl,y_pl, 'o', label="Limits")
plt.plot(x,y_new1*np.ones(len(x)),'g--' ,label = "10 percent Threshold", linewidth = 0.85)
plt.plot(x,y_new2*np.ones(len(x)),'g--' ,label = "10 percent Threshold", linewidth = 0.85)
plt.legend()
plt.show()
plt.close()
