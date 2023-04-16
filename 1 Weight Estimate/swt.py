import numpy as np
import matplotlib.pyplot as plt
import math

we = [4276, 7070, 4803, 14741, 20600, 8310, 1150, 1995.8, 23200#,46700]
]
w0 = [7530, 11500, 10660, 26380, 32600, 11860, 1635, 2540.1, 41600#,67700]
]
weng = [312, 782, 684, 1760, 2424, 688, 302, 290, 4354#,2908]
]
we_weng_w0 = [0.5264276228, 0.5467826087, 0.3863977486, 0.4920773313, 0.5575460123, 0.6426644182, 0.5186544343, 0.6715483642, 0.4530288462#,0.6468537666]
]

log_w0 = []
log_we_weng_w0 = []

for i in range(0, len(w0)):
    log_w0.append(math.log(w0[i]))
    log_we_weng_w0.append(math.log(we_weng_w0[i]))

m, c = np.polyfit(log_w0, log_we_weng_w0, 1)
A = math.e ** c
L = m
print(A, L)

x_axis = np.linspace(min(log_w0), max(log_w0), 50)
y_axis = m*x_axis + c

plt.figure()
plt.grid(linestyle='--')
plt.title("Logarithmic scale plot for Empty Wt Ratio vs MTOW")
plt.xlabel("log($W_0$)")
plt.ylabel("log(${W_e}$/${W_0}$)")
plt.plot(log_w0, log_we_weng_w0, '.', label='Scatter Plot')
plt.plot(x_axis, y_axis, label='Linear Best Fit Line')
plt.legend()
plt.show()
plt.close()


x_axis = np.linspace(min(w0), max(w0), 50)
y_axis = A*x_axis**L
plt.figure()
plt.grid(linestyle='--')
plt.title("Plot for Empty Wt Ratio vs MTOW")
plt.xlabel("$W_0$")
plt.ylabel("${W_e-w_{eng}}$/${W_0}$")
plt.plot(w0, we_weng_w0, '.', label='Scatter Plot')
plt.plot(x_axis, y_axis, label='Best Fit Curve')
plt.legend()
plt.show()
plt.close()

w_pl = float(input("Enter W_pl : "))
w_guess = float(input("Enter Initial W_0 Guess : "))

w_cr = 210
w_f = 0.1997
tol = 0.000001
w_eng = 3449*2 # Rolls Royce RB211 535E4 C37 - High BP Turbofan, net thrust = 189.2 kN

arr = [w_guess]
iter = [0]


def main(w_guess_arg):
    w_old = w_guess_arg
    for i in range(0, 100):
        wew0 = A*w_old**L
        w_new = float(w_cr + w_pl + w_eng)/(1 - w_f - wew0 + w_eng/w_old)
        arr.append(w_new)   
        iter.append(i+1)

        if (abs(w_new - w_old) < tol):
            print("got weight")
            break
        else:
            w_old = w_new


main(w_guess)

print(arr[-1])

plt.figure()
plt.grid(linestyle='--')
plt.title("Estimted Wt vs No. of Iterations")
plt.xlabel("No. of Iterations")
plt.ylabel("Estimated Weight")
plt.plot(iter, arr, '.-', label="Estimated weight")
plt.legend()
plt.show()
