import numpy as np
import matplotlib.pyplot as plt

# Função que computa as derivadas do problema SIR
def deriv(S, I, R, beta, gamma):
    dS = -beta * S * I 
    dI = beta * S * I - gamma * I
    dR = gamma * I
    return dS, dI, dR

# Valores iniciais do problema
I0 = 1
R0 = 0
S0 = 50
T = 24

# Pelo enunciado, sabemos que na outra escola o número de suscetíveis era 40 e infectados eram 8 e passou a ser 30 e 18, respectivamente.
# Então, N será 10 (10 alunos passaram de suscetíveis para infectados)

N = 10

# Pelo enunciado, sabemos que dos 15 infectados, 3 se recuperaram

m = 3
n = 15

# Gamma e beta para periodos de 24h (1 dia).

beta = N/(T*S0*I0)
gamma = m/(n*T)

# Parametros para a função de Euler
t_max = 200
dt = 1  # Tamanho do intervalo temporal (Seria o h da função utilizada no colab)

# Listas para guardar os valores das funções
S_values = [S0]
I_values = [I0]
R_values = [R0]
t_values = [0]

# Método de Euler
for t in range(1, t_max + 1):
    dS, dI, dR = deriv(S_values[-1], I_values[-1], R_values[-1], beta, gamma)
    S = S_values[-1] + dS * dt
    I = I_values[-1] + dI * dt
    R = R_values[-1] + dR * dt

    S_values.append(S)
    I_values.append(I)
    R_values.append(R)
    t_values.append(t)

# Plotar resultados
plt.plot(t_values, S_values, label='Suscetíveis')
plt.plot(t_values, I_values, label='Infectados')
plt.plot(t_values, R_values, label='Recuperados')
plt.xlabel('Tempo (dias)')
plt.ylabel('População')
plt.legend()
plt.show()
