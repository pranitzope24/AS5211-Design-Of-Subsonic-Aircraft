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
y = np.linspace(0.0472, 0.0966,12000)
y1 = []
y2 = []

def hmax1(x):
    return 2*(7474.084)*(F_1/x + F_2)

def hmax2(x):
    return np.sqrt(4*k*(F_1 + F_2*x))



min_y1 = 1000000000000
min_x1 = 0
for i in range(0,len(x)):
    y1.append(hmax1(x[i]))
    curr1 = hmax1(x[i])
    if(min_y1>curr1):
        min_y1 = curr1
        min_x1 = x[i]

min_y2 = 1000000000000
min_x2 = 0
for i in range(0,len(x)):
    y2.append(hmax2(x[i]))
    curr2 = hmax2(x[i])
    if(min_y2>curr2):
        min_y2 = curr2
        min_x2 = x[i]

xr = 5676.45
yr = 0.0661769

y_new1 = yr+ 0.05*yr
y_new2 = yr- 0.05*yr

x_l = 5140 
x_r = 6338.24

plt.figure()
plt.grid(linestyle='--')
plt.title("Plot for Max. Height")
plt.xlabel("P")
plt.ylabel("(T/W)")
plt.plot(x, y1, '-', label='1')
plt.plot(x, y2, '-', label='2')

# plt.plot(min_x, min_y, 'o', label="Minimum Value")
# plt.plot(x_pl,y_pl, 'o', label="5 percent Thershold")
plt.plot(x,y_new1*np.ones(len(x)),'g--' ,label = "1",linewidth = 0.85)
plt.plot(x,y_new2*np.ones(len(x)),'g--' ,label = "2", linewidth = 0.85)
plt.plot(x_l*np.ones(len(y)), y,'r--',label = "1", linewidth = 0.85)
plt.plot(x_r*np.ones(len(y)), y,'r--',label = "2", linewidth = 0.85)


plt.legend()
plt.show()
plt.close()