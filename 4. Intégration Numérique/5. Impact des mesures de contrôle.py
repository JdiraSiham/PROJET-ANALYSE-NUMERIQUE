import numpy as np 
# Paramètres 
N = 36000000 
a = 0.014 
b = 0.0040108 
r_initial = 0.04108 
r_control = 0.025  # taux réduit après mesures 
dt = 10 
T = 500 
# Conditions initiales 
I0 = 1 
R0 = 0 
D0 = 0 
S0 = N - I0 - R0 - D0 
def sird_simulation(r): 
    S, I, R, D = S0, I0, R0, D0 
    for _ in range(0, T, dt): 
        dS = -r * S * I / N 
        dI = r * S * I / N - (a + b) * I 
        dR = a * I 
        dD = b * I 
 
        S += dS * dt 
        I += dI * dt 
        R += dR * dt 
        D += dD * dt 
 
    total_infected = N - S 
    return total_infected 
 
# Simulation sans mesure 
infected_initial = sird_simulation(r_initial) 
 
# Simulation avec mesure de contrôle 
infected_control = sird_simulation(r_control) 
# Calcul de l'impact 
reduction = infected_initial - infected_control 
pourcentage = (reduction / infected_initial) * 100 
print("Total infectés sans mesure :", int(infected_initial)) 
print("Total infectés avec mesure :", int(infected_control)) 
print("Réduction due à la mesure  :", int(reduction)) 
print("Impact en pourcentage      :", round(pourcentage, 2), "%")
