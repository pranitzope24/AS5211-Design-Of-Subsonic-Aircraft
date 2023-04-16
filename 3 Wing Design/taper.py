lam = 0.5 #change
ar = 8.5
b = 36.1
r = 0.3 #change
s = b**2/ar

cr = s/((r*b) + (1+lam)*(1-r)*(b/2))
ct = lam*cr
c = 2*cr*(1+lam+lam**2)/((1+lam)*3)

print(cr,ct,c)