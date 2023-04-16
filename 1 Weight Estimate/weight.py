import numpy as np
import matplotlib.pyplot as plt
import math


we_w0 = [0.5678618858, 0.6147826087, 0.4505628518, 0.5587945413,
         0.7006745363, 0.6319018405, 0.7033639144, 0.7857170978, 0.5576923077, 0.6898079]
w0 = [7530, 11500, 10660, 26380, 11860, 32600, 1635, 2540.1, 41600,67700]
log_w0 = []
log_we_w0 = []

for i in range(0, len(w0)):
    log_w0.append(math.log(w0[i]))
    log_we_w0.append(math.log(we_w0[i]))

m, c = np.polyfit(log_w0, log_we_w0, 1)
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
plt.plot(log_w0, log_we_w0, '.', label='Scatter Plot')
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
plt.ylabel("${W_e}$/${W_0}$")
plt.plot(w0, we_w0, '.', label='Scatter Plot')
plt.plot(x_axis, y_axis, label='Best Fit Curve')
plt.legend()
plt.show()
plt.close()

w_pl = float(input("Enter W_pl : "))
w_guess = float(input("Enter Initial W_0 Guess : "))

w_cr = 210
w_f = 0.1997
tol = 0.000001

A, L = 1.2603034953464771, -0.07802256194417133


def MTOW(w_guess_arg):
    w_e_final = (A*w_guess_arg**L)
    return float(w_cr + w_pl)/(1 - w_f - w_e_final)


arr = [w_guess]
iter = [0]


def main(w_guess_arg):
    w_old = w_guess_arg
    for i in range(0, 100):
        wew0 = A*w_old**L
        w_new = float(w_cr + w_pl)/(1 - w_f - wew0)
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
