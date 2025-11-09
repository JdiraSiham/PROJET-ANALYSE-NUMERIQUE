import numpy as np 
import matplotlib.pyplot as plt 
 
jours = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 
         151, 161, 171, 181, 191, 201, 211, 221, 231, 241, 251, 261, 271, 
         281, 291, 301, 311, 321, 331, 341, 351, 361, 371, 381, 391, 401, 
         411, 421, 431, 441, 451, 461, 471, 481, 491, 500] 
 
I_cumule = np.array([1, 5, 86, 617, 1431, 3209, 4423, 6063, 7133, 7780, 
                     8437, 9613, 12248, 14771, 17236, 20278, 27217, 38805, 58489, 
                     72394, 94504, 119107, 140024, 173632, 203733, 246349, 293177, 
                     340684, 376738, 406970, 430562, 443146, 456334, 469139, 478135, 
                     480056, 482994, 485974, 488632, 491463, 494659, 497832, 500948, 
                     504260, 507938, 511562, 515023, 518868, 522765, 526651, 566356]) 
guerisons = [0, 1, 3, 24, 105, 393, 984, 2554, 4098, 5401, 7493, 8117, 
             8740, 11316, 14921, 16438, 19629, 26687, 43049, 55274, 74930, 
             97468, 118142, 143972, 168706, 202491, 238276, 289808, 327693, 
             365036, 396276, 415829, 431167, 445250, 456032, 463271, 468387, 
             470425, 472991, 477911, 482352, 484793, 487414, 490366, 493873, 
             497382, 503483, 507681, 511842, 513681, 536620] 
 
deces = [0, 1, 3, 36, 105, 145, 170, 188, 248, 294, 336, 380, 424, 482, 540, 603, 
         684, 784, 902, 1012, 1174, 1323, 1490, 1653, 1833, 2023, 2233, 2455, 2701, 
         2950, 3210, 3481, 3763, 4056, 4350, 4654, 4960, 5277, 5605, 5944, 6293, 
         6652, 7021, 7399, 7788, 8187, 8596, 9015, 9444, 9883, 10332] 
 
N_pop = 36000000 
a = 0.014057 
b = 0.004022 
r = 0.04108 
 
# Approximation des infectés actifs par différence (valeurs instantanées ≈ dérivées) 
I = np.diff(I_cumule, prepend=I_cumule[0]) 
 
 
S = N_pop - I_cumule-guerisons-deces 
 
# Calcul de dI/dt théorique 
dI_model = r * S * I - (a + b) * I 
 
# Détection de décroissance sur au moins N jours consécutifs 
N_consec = 4 
debut_declin = None 
 
for i in range(len(dI_model) - N_consec): 
    if all(dI_model[i + k] > dI_model[i + k + 1] for k in range(N_consec)): 
        debut_declin = jours[i] 
        break 
 
# Affichage graphique 
plt.figure(figsize=(12, 6)) 
plt.plot(jours, dI_model, label="Variation théorique dI/dt", color='blue') 
if debut_declin: 
    plt.axvline(debut_declin, color='red', linestyle='--', label=f"Début décroissance (jour 
{debut_declin})") 
plt.xlabel("Jour") 
plt.ylabel("Variation théorique dI/dt") 
plt.title("Détection de la décroissance épidémique (modèle SIRD)") 
plt.legend() 
plt.grid(True) 
plt.tight_layout() 
plt.show()
