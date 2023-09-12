'''
Bla bla bla mr freeman
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#Função dada:
P_0 = lambda t: 1
P_1 = lambda t: t 


P_list = [P_0, P_1]
def recursive_lambda(d):
        return lambda t, f1=P_list[-1], f2=P_list[-2]: (((2*d + 1)/(d+1))*t*f1(t)) - (((d)/(d+1))*f2(t))
#Indexando todas as funções em uma lista
for d in range(1,6):
    P_list.append(recursive_lambda(d))

#Pode ser utilizado método da bisseção
def bissecao (f,a,b,tol):
    if(f(a)*f(b)<0):
        c = (a+b)/2
        if(abs(f(c)) < tol): return c
        if(f(a)*f(c)<0):
            return bissecao(a,c,f)
        elif(f(b)*f(c)<0):
            return bissecao(c,b,f)  
    else:
        print("Nao foi possivel encontrar raiz") 
        return 0  
    
#Bizu para ver aproximadamente os intervalos que vc vai utilizar para o zero (Estão todos entre 0 e 1)    
# def plot_graphs():
#     x = np.linspace(0,1,100)
#     y_g = P_list[2](x)
#     y_h = P_list[3](x)
#     y_i = P_list[4](x)
#     y_j = P_list[5](x)
#     y_k = P_list[6](x)
#     y_l = P_list[1](x)
#     plt.plot(x,y_i,label='wharevis')
#     plt.plot(x,y_j,label='h(x) = x')
#     plt.plot(x,y_k,label='wharevis')
#     plt.plot(x,y_l,label='h(x) = x')
#     plt.plot(x,y_g,label='wharevis')
#     plt.plot(x,y_h,label='h(x) = x')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.show()  
# plot_graphs()

initial_guess = 0.5
p_solution = fsolve(P_list[4], initial_guess)
print(p_solution)

#OLHA O GRAFICO PLOTADO, FAZ UM INITIAL GUESS, DESCOBRE O VALOR, ANOTA OU BOTA EM UMA LISTA OU DICT!!!!!! 
#SE QUISER DEIXAR BONITO BASTA FAZER UM DATAFRAME COM PANDAS (NAO PRECISA, SÓ SE SOUBER OQ ESTÁ FAZENDO)