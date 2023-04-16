import numpy as np
import matplotlib.pyplot as plt
import math

F_1 = 0.01203321162
F_2 = 0.000002307238425
k = 0.04356653045
V_c = 12.7*np.sqrt(0.3218995598)
rho = 1.225
a = [-0.00139829, 0.76439155]
kt = 1.43
cfe = 0.0033
swet_wing = 266.33
s_old = 153.3
cd0 = 0.0239
w_s_old = 5176.06
e = 0.86
AR = 8.5
rho = 0.466
v = 236.111
q = 0.5*rho*v**2
f1 = kt*cfe*((swet_wing)/s_old)
f2 = (cd0-f1)/(w_s_old)
f3 = (1/math.pi)*(1/(AR*e*q**2))

x = np.linspace(3000, 12000, 12000)
y = np.linspace(0, 0.30, 12000)


def roc(x):
    ans = (V_c/(np.sqrt(x))+0.04579280643+(2.307238425*pow(10, -6))
           * (x))/(a[0]*np.sqrt(x/0.3218995598)+a[1])
    return ans


def hmax1(x):
    return 2*(7474.084)*(F_1/x + F_2)


def hmax2(x):
    return np.sqrt(4*k*(F_1 + F_2*x))


def prec_vel(x):
    y = q*(f1/x + f2 + f3*x)
    return y


def sland(x):
    y = x/2.632908425
    return y


def rng(p):
    ans = 1264.61074551*(0.01203321162/p+2.307*10**(-6)+4.187*10**(-10) * p)
    return ans


x_roc = [3920.13, 11410.3]
x_hmax = [5140, 6338.24]
x_r = [3640.06, 7891.64]
x_vp = [3600, 8823.46]
x_sl = [4263.52, 5212.26]

plt.figure()
plt.title("Thrust Loading vs Wing Loading for all Parameters", fontsize=15)
plt.xlabel("(W/S) (N/$m^2$)", fontsize=15)
plt.ylabel("(T/W)", fontsize=15)

plt.plot(x, roc(x), 'b', label="rate of Climb")
plt.plot(x_roc[1]*np.ones(len(y)), y, 'b', label="ROC Limits", linewidth=0.85)
plt.plot(x_roc[1]*np.ones(len(y)), y, 'b', label="ROC Limits", linewidth=0.85)

plt.plot(x, rng(x), 'g', label="Range")
plt.plot(x_r[0]*np.ones(len(y)), y, 'g', label="Range Limits", linewidth=0.85)
plt.plot(x_r[1]*np.ones(len(y)), y, 'g', label="Range Limits", linewidth=0.85)

plt.plot(x, hmax1(x), 'm', label="H_max 1")
plt.plot(x, hmax2(x), 'm', label="H_max 2")
plt.plot(x_hmax[0]*np.ones(len(y)), y, 'm',
         label="H_max Limits", linewidth=0.85)
plt.plot(x_hmax[1]*np.ones(len(y)), y, 'm',
         label="H_max Limits", linewidth=0.85)

plt.plot(x, prec_vel(x), 'r', label="Prescreibed Velocity")
plt.plot(x_vp[0]*np.ones(len(y)), y, 'r', label="V_p Limits", linewidth=0.85)
plt.plot(x_vp[1]*np.ones(len(y)), y, 'r', label="V_p Limits", linewidth=0.85)

# plt.plot(x,sland(x), label = "Landing Disance")
plt.plot(x_sl[0]*np.ones(len(y)), y, 'y',
         label="S_land Limits", linewidth=0.85)
plt.plot(x_sl[1]*np.ones(len(y)), y, 'y',
         label="S_land Limits", linewidth=0.85)

plt.plot(5212, roc(5212), 'o', color="black", label="Selected Point")

plt.fill_between(x, 0.3, -0.01, where=(x > 5140) &
                 (x < 5212), color='c', alpha=0.3)

plt.legend(loc=1)
plt.show()
plt.close()
print(roc(5212))
