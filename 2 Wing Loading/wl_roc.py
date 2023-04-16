import numpy as np
import matplotlib.pyplot as plt
import math

F_1 = 0.01203321162
F_2 = 0.000002307238425
k = 0.04356653045
V_c = 12.7*np.sqrt(0.3218995598)
rho = 1.225
a=[-0.00139829, 0.76439155]
x = np.linspace(3000, 12000, 12000)

y = []

def fun1(x):
    ans = (V_c/(np.sqrt(x))+0.04579280643+(2.307238425*pow(10, -6))
           * (x))/(a[0]*np.sqrt(x/0.3218995598)+a[1])
    return ans

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
y_new += min_y*0.05

print(y_new)

3920.13
11410.3

x_pl = [3920.13, 11410.3]
y_pl = [fun1(3920.13), fun1(11410.3)]


plt.figure()
plt.grid(linestyle='--')
plt.title("Plot for Rate of Climb")
plt.xlabel("P")
plt.ylabel("(T/W))")
plt.plot(x, fun1(x), '-', label='Thrust Loading vs Wing Loading')
plt.plot(min_x, min_y, 'o', label="Minimum Value")
plt.plot(x_pl,y_pl, 'o', label="5 percent Thershold")
plt.plot(x,y_new*np.ones(len(x)),'--' ,label = "5 percent Threshold")

plt.legend()
plt.show()
plt.close()