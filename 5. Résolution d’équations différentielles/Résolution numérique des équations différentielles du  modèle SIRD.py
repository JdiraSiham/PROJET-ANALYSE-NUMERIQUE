import numpy as np 
# Paramètres 
N = 36000000          
a = 0.014             
b = 0.0040108         
r = 0.04108           
dt = 10               
T = 500               
# Population totale 
# Taux de guérison 
# Taux de mortalité 
# Taux de transmission 
# Pas de temps (en jours) 
# Durée totale de simulation (en jours) 
# Conditions initiales 
I0 = 1 
R0 = 0 
D0 = 0 
S0 = N - I0 - R0 - D0 
# Fonction du modèle SIRD 
def sird_deriv(S, I, R, D): 
dS = -r * S * I / N 
dI = r * S * I / N - (a + b) * I 
dR = a * I 
dD = b * I 
return dS, dI, dR, dD 
# Initialisation des listes 
S, I, R, D = [S0], [I0], [R0], [D0] 
time = [0] 
# Résolution du système par méthode de Runge-Kutta ordre 4 
for t in range(1, T // dt + 1): 
S_t, I_t, R_t, D_t = S[-1], I[-1], R[-1], D[-1] 
k1 = sird_deriv(S_t, I_t, R_t, D_t) 
k2 = sird_deriv(S_t + dt/2*k1[0], I_t + dt/2*k1[1], R_t + dt/2*k1[2], 
D_t + dt/2*k1[3]) 
k3 = sird_deriv(S_t + dt/2*k2[0], I_t + dt/2*k2[1], R_t + dt/2*k2[2], 
D_t + dt/2*k2[3]) 
k4 = sird_deriv(S_t + dt*k3[0], I_t + dt*k3[1], R_t + dt*k3[2], D_t + 
dt*k3[3]) 
S_next = S_t + dt/6 * (k1[0] + 2*k2[0] + 2*k3[0] + k4[0]) 
I_next = I_t + dt/6 * (k1[1] + 2*k2[1] + 2*k3[1] + k4[1]) 
R_next = R_t + dt/6 * (k1[2] + 2*k2[2] + 2*k3[2] + k4[2]) 
D_next = D_t + dt/6 * (k1[3] + 2*k2[3] + 2*k3[3] + k4[3]) 
S.append(S_next) 
I.append(I_next) 
R.append(R_next) 
D.append(D_next) 
time.append(t * dt) 
# Résultat final 
print("Jour final :", time[-1]) 
print("Sains (S)   :", int(S[-1])) 
print("Infectés (I):", int(I[-1])) 
print("Guéris (R)  :", int(R[-1])) 
print("Décès (D)   :", int(D[-1]))
