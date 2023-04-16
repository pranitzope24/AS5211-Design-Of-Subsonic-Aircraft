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


kt=1.43
cfe=0.0033
swet_wing=266.33
s_old=153.3
cd0=0.0239
w_s_old=5176.06
e=0.86
AR=8.5
rho=0.466
v=236.111
q=0.5*rho*v**2
f1=kt*cfe*((swet_wing)/s_old)
f2=(cd0-f1)/(w_s_old)
f3=(1/math.pi)*(1/(AR*e*q**2))

y = []

def fun(x):
    y = q*(f1/x + f2 + f3*x)
    return y

min_y = 1000000000000
min_x = 0
for i in range(0,len(x)):
    y.append(fun(x[i]))
    curr = fun(x[i])
    if(min_y>curr):
        min_y = curr
        min_x = x[i]

print (min_x)

y_new = min_y
y_new += min_y*0.05

print(y_new)


x_pl = [3600, 8823.46]
y_pl = [fun(3600), fun(8823.46)]


plt.figure()
plt.grid(linestyle='--')
plt.title("Plot for Prescribed Velocity")
plt.xlabel("(W/S)")
plt.ylabel("(T/W)")
plt.plot(x, fun(x), '-')
plt.plot(min_x, min_y, 'o', label="Minimum Value")
plt.plot(x_pl,y_pl, 'o', label="Limits")
plt.plot(x,y_new*np.ones(len(x)),'--' ,label = "5 percent Threshold")

plt.legend()
plt.show()
plt.close()