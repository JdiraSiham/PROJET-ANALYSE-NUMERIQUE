#Analyse de la vitesse de propagation du virus dans différentes régions : (ex :Casa-settat et Souss-Massa) 

import matplotlib.pyplot as plt 
import numpy as np 
 
 
jours = [1, 3, 5, 8, 9, 11, 13, 14, 17, 20, 22] 
 
# Données infectés (non cumulés) 
casablanca = [1,645, 1141, 1731, 2193, 3141, 3701, 4494, 5744, 7323, 8009] 
souss_massa = [0,42, 96, 140, 169, 278, 278, 352, 487, 684, 733] 
 
 
jours = np.array(jours) 
casablanca = np.array(casablanca) 
souss_massa = np.array(souss_massa) 
 
# Calcul des vitesses ΔI/Δt 
delta_t = np.diff(jours) 
vitesse_casa = np.diff(casablanca) / delta_t 
vitesse_souss = np.diff(souss_massa) / delta_t 
jours_vitesse = (jours[:-1] + jours[1:]) / 2 
 
 
plt.figure(figsize=(12, 5)) 
 
plt.subplot(1, 2, 1) 
plt.plot(jours, casablanca, label='Casablanca-Settat', marker='o') 
plt.plot(jours, souss_massa, label='Souss-Massa', marker='s') 
plt.title('Cas infectés ') 
plt.xlabel('Jour') 
plt.ylabel('Cas') 
plt.grid(True) 
plt.legend() 
 
plt.subplot(1, 2, 2) 
plt.plot(jours_vitesse, vitesse_casa, label='Propagation Casablanca', marker='o') 
plt.plot(jours_vitesse, vitesse_souss, label='Propagation Souss-Massa', marker='s') 
plt.title('Vitesse de propagation (ΔI / Δt)') 
plt.xlabel('Jour (milieu de l\'intervalle)') 
plt.axhline(0, color='gray', linestyle='--') 
plt.ylabel('Δ cas / jour') 
plt.grid(True) 
plt.legend() 
 
plt.tight_layout() 
plt.show() 
