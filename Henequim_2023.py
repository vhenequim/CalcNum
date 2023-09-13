import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#Constantes

X = 596915.961
Y = -4847845.536
Z = 4088158.163
a = 6378137
b = 6356752.3142
tol = 10**-6
W = (X**2 + Y**2)**(0.5)

#Função f(m) contendo a raiz m necessária para o restante do problema
f = lambda m: (W**2/(a + 2*m/a)**2) + (Z**2/(b + 2*m/b)**2) - 1
df = lambda m: -((4*a**2*W**2)/(a**2 + 2*m)**3)-((4*b**2*Z**2)/(b**2+2*m)**3)

#Chute inicial ('_')
m0 = (a*b*((a*Z)**2+(b*W)**2)**(3/2) - (a*b)**2*((a*Z)**2+(b*W)**2)) / (2*(a**4*Z**2 + b**4*W**2))

#Raiz será o f_solution  
# initial_guess = m0
# f_solution = fsolve(f, initial_guess)
# print(f_solution)

#Definindo Newton-Raphson
def newton(f, df, x0, TolX, MaxIter):
    h = 1e-4
    h2 = 2 * h
    TolFun = np.finfo(float).eps
    xx = [x0]
    fx = f(x0)

    for k in range(MaxIter):
        if not isinstance(df, (int, float)):
            dfdx = df(xx[k])
        else:
            dfdx = (f(xx[k] + h) - f(xx[k] - h)) / h2

        dx = -fx / dfdx
        xx.append(xx[k] + dx)
        fx = f(xx[k + 1])

        if abs(fx) < TolFun or abs(dx) < TolX:
            break

    x = xx[-1]

    if k == MaxIter:
        print(f"The best in {MaxIter} iterations")

    return x, fx, xx

mx, fx, xx = newton(f, df, m0, tol, MaxIter=100)

#Definindo os valores para a resposta:
cor = (1+2*mx/a**2) #correção para os We, Xe, Ye. Ze é diferente
We = abs(W/(cor))
Ze = Z/(1+2*mx/b**2)
Xe = X/cor
Ye = Y/cor
phirad = np.arctan((a**2*Ze)/(b**2*We))
lmbrad= np.arctan(Y/Z)
phi = round(np.degrees(phirad), 4) #Latitude
lmb = round(np.degrees(lmbrad), 4) #Longitude
h = round(((W-We)**2+(Z-Ze)**2)**(0.5), 4)
if (W + abs(Z)) < (We + abs(Ze)):
    h = -h
print("Os valores são:\n Latitude: ", phi, "\nLongitude: ", lmb, "\nAltitude: ", h)


