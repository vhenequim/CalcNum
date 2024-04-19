import scipy
import numpy as np
import pandas as pd

# Declaração de algumas constantes e variáveis
f = 1/298.257222101
E = np.sqrt((2 - f) * f)
E_sqr = (2-f) * f
a = 6378.137
phi = 90
degree = np.deg2rad(phi)


# Declaração da função do meridiano
def m_integral(phi):
    return (1 - (E_sqr * (np.sin(phi))**2) )**(-3/2) * a * (1 - E_sqr) 

# Declaração da função do paralelo
def l_func(phi, delta_lambda):
    N = a/np.sqrt(1 - (E_sqr*(np.sin(phi))**2))
    return N*np.cos(phi)*delta_lambda


# Listas com os angulos
phi_list = [0, 15, 30, 45, 60, 75, 90]
phi_1_deg = []
phi_1_min = []
phi_1_sec = []
lambda_1_deg = []
lambda_1_min = []
lambda_1_sec = []
phi_delta = [np.deg2rad(1), np.deg2rad(1/60), np.deg2rad(1/3600)]

# Fazendo contas pro meridiano e paralelo para cada tipo de delta
# Fazer um loop com todos os deltas parece dar problema de escopo, resultados modificam (obg python xd)
for main_phi in phi_list:
    result, _ = scipy.integrate.quad(m_integral, np.deg2rad(main_phi),np.deg2rad(main_phi + 1))
    phi_1_deg.append(result)

    lambda_1_deg.append(np.round(l_func(np.deg2rad(main_phi),np.deg2rad(1)), decimals=6))

for main_phi in phi_list:
    result, _ = scipy.integrate.quad(m_integral, np.deg2rad(main_phi),np.deg2rad(main_phi + 1/60))
    phi_1_min.append(result)

    lambda_1_min.append(np.round(l_func(np.deg2rad(main_phi),np.deg2rad(1/60)), decimals=6))

for main_phi in phi_list:
    result, _ = scipy.integrate.quad(m_integral, np.deg2rad(main_phi),np.deg2rad(main_phi + 1/3600))
    phi_1_sec.append(result) 

    lambda_1_sec.append(np.round(l_func(np.deg2rad(main_phi),np.deg2rad(1/3600)), decimals=6))

data = list(zip(phi_list, phi_1_deg, phi_1_min, phi_1_sec,
                lambda_1_deg, lambda_1_min, lambda_1_sec))

df = pd.DataFrame(data, columns=["Phi", "Delta 1 Deg", "Delta 1 Min", "Delta 1 Sec", "Lambda 1 Deg",
                                 "Lambda 1 Min", "Lambda 1 Sec"])

print(df)


