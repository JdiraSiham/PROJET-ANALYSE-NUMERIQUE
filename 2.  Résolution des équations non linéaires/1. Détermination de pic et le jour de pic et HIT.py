import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
 
# Données cumulées 
data = { 
    'Jour': [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 
121, 131, 141, 151, 161, 171, 181, 191, 201, 211, 221, 231, 241, 
251, 261, 271, 281, 291, 301, 311, 321, 331, 341, 351, 361, 371, 
381, 391, 401, 411, 421, 431,  441, 451, 461, 471, 481, 491, 
500], 
    'Date': ['01/03/2020', '11/03/2020', '21/03/2020', 
'31/03/2020', '10/04/2020',  '20/04/2020', '30/04/2020', 
'10/05/2020', '20/05/2020', '30/05/2020', '09/06/2020', 
'19/06/2020', '29/06/2020', '09/07/2020', '19/07/2020', 
'29/07/2020', '08/08/2020', '18/08/2020', '28/08/2020', 
'07/09/2020', '17/09/2020', '27/09/2020', '07/10/2020', 
'17/10/2020', '27/10/2020', '06/11/2020', '16/11/2020', 
'26/11/2020', '06/12/2020', '16/12/2020',  '26/12/2020', 
'05/01/2021', '15/01/2021', '25/01/2021', '04/02/2021', 
'14/02/2021','24/02/2021', '06/03/2021', '16/03/2021', 
'26/03/2021',  '05/04/2021', '15/04/2021', '25/04/2021', 
'05/05/2021', '15/05/2021', '25/05/2021', '04/06/2021', 
'14/06/2021', '24/06/2021', '04/07/2021', '13/07/2021'], 
    'Infectés_cumul': [1, 5, 86, 617, 1431, 3209, 4423, 6063, 
7133, 7780, 8437, 9613, 12248, 14771, 17236, 20278, 27217, 38805, 
58489, 72394, 94504,119107, 140024, 173632, 203733, 246349, 
293177, 340684, 376738,406970, 430562, 443146, 456334, 469139, 
478135, 480056, 482994,485974, 488632, 491463, 494659, 497832, 
500948, 504260, 507938,511562, 515023, 518868, 522765, 526651, 
566356], 
    'Rétablis_cumul' : [0, 1, 3, 24, 105, 393, 984, 2554, 4098, 
5401, 7493, 8117, 8740, 11316, 14921, 16438, 19629, 26687, 43049, 
55274, 74930, 97468,118142, 143972, 168706, 202491, 238276, 
289808, 327693, 365036, 396276, 415829, 431167, 445250, 456032, 
463271, 468387, 470425,472991, 475911, 482352, 484793, 487414, 
490366, 493873, 497382, 503483, 507681, 511842, 513681, 536626], 
    'Décédés_cumul': [0, 1, 3, 36, 105, 145, 170, 188, 194, 204, 
210, 213, 224, 242, 273, 313, 417, 584, 1052, 1361, 1714, 2113, 
2439, 2928, 3445,4079, 4829, 5619, 6184, 6740, 7240, 7485, 7784, 
8224, 8466, 8540,8608, 8653, 8693, 8745, 8798, 8842, 8882, 8940, 
9000, 9060, 9104, 9160, 9220, 9238, 9498] 
} 
df = pd.DataFrame(data) 
df['Nouveaux_infectés'] = 
df['Infectés_cumul'].diff().fillna(df['Infectés_cumul'].iloc[0]) 
df['Nouveaux_rétablis'] = 
df['Rétablis_cumul'].diff().fillna(df['Rétablis_cumul'].iloc[0]) 
df['Nouveaux_décédés'] = 
df['Décédés_cumul'].diff().fillna(df['Décédés_cumul'].iloc[0]) 
df['Actifs'] = df['Infectés_cumul'] - df['Rétablis_cumul'] - 
df['Décédés_cumul'] 
pic_index = df['Actifs'].idxmax() 
pic_jour = df.loc[pic_index, 'Jour'] 
pic_date = df.loc[pic_index, 'Date'] 
pic_actifs = df.loc[pic_index, 'Actifs'] 
print(f"Pic épidémique:") 
print(f"- Jour: {pic_jour}") 
print(f"- Date: {pic_date}") 
print(f"- Nombre de cas actifs: {int(pic_actifs)}") 
a_est = df['Nouveaux_rétablis'].sum() / df['Actifs'].sum() 
b_est = df['Nouveaux_décédés'].sum() / df['Actifs'].sum() 
N = 36000000   
df['S'] = N - df['Infectés_cumul'] 
df['dI_dt'] = df['Actifs'].diff().fillna(0)   
df['r_estimé'] = (df['dI_dt'] + (a_est + b_est) * df['Actifs']) / 
(df['S'] * df['Actifs']) 
df['r_estimé'] = df['r_estimé'].replace([np.inf, -np.inf], 
np.nan)   
r_est = df['r_estimé'].median()  
Sc = (a_est + b_est) / r_est if r_est > 0 else 0 
Pc = 1 - Sc/N if N > 0 else 0 
print("\nParamètres estimés:") 
print(f"- Taux de transmission (r): {r_est:.8f}") 
print(f"- Taux de guérison (a): {a_est:.6f}") 
print(f"- Taux de mortalité (b): {b_est:.6f}") 
print("\nSeuil d'immunité collective:") 
print(f"- Seuil critique (Sc): {Sc:.1f} personnes") 
print(f"- Proportion à immuniser (Pc): {Pc:.2%}") 
# Visualisation 
plt.figure(figsize=(14, 7)) 
# Cas actifs 
plt.subplot(2, 1, 1) 
plt.plot(df['Jour'], df['Actifs'], label='Cas actifs') 
plt.axvline(x=pic_jour, color='r', linestyle='--', label=f'Pic 
épidémique (Jour {pic_jour})') 
plt.title('Évolution des cas actifs et pic épidémique') 
plt.xlabel('Jours') 
plt.ylabel('Cas actifs') 
plt.legend() 
plt.grid() 
 
# Nouveaux cas 
plt.subplot(2, 1, 2) 
plt.bar(df['Jour'], df['Nouveaux_infectés'], color='orange', 
alpha=0.7, label='Nouveaux infectés') 
plt.title('Nouveaux cas par jour') 
plt.xlabel('Jours') 
plt.ylabel('Nouveaux cas') 
plt.legend() 
plt.grid() 
 
plt.tight_layout() 
plt.show()


#RECHERCHE DU TEMPS CRITIQUE : 

import matplotlib.pyplot as plt 
# Données (jours et cas cumulés confirmés) 
jours = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 
         151, 161, 171, 181, 191, 201, 211, 221, 231, 241, 251, 261, 271, 
         281, 291, 301, 311, 321, 331, 341, 351, 361, 371, 381, 391, 401, 
         411, 421, 431, 441, 451, 461, 471, 481, 491, 500] 
 
cas = [1, 5, 86, 617, 1431, 3209, 4423, 6063, 7133, 7700, 8437, 9613, 
       12248, 14771, 17236, 20278, 27217, 38805, 58489, 72394, 94504, 
       119107, 140024, 173632, 203733, 246349, 293177, 340684, 376738, 
       406970, 436962, 443146, 456324, 469139, 478135, 480056, 482994, 
       485974, 488623, 494463, 494465, 497832, 500948, 504260, 507938, 
       511562, 515023, 518965, 522765, 526651, 566356] 
 
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
 
# Calcul des infectés actifs : I(t) = cas cumulés - guérisons - décès 
infectes_actifs = [cas[i] - guerisons[i] - deces[i] for i in range(len(jours))] 
# Seuil critique Imax 
Imax = 50072 # Capacité maximale estimée du système hospitalier 
 
# Recherche du jour où I(t) dépasse Imax 
tc = None 
for i, I in enumerate(infectes_actifs): 
    if I > Imax: 
        tc = jours[i]+10 
        break 
 
# Affichage des résultats 
plt.figure(figsize=(10, 5)) 
plt.plot(jours, infectes_actifs, label="Infectés actifs") 
plt.axhline(Imax, color='red', linestyle='--', label=f"Imax = {Imax}") 
if tc: 
plt.axvline(tc, color='orange', linestyle='--', label=f"Intervention critique (jour {tc})") 
print(f" Temps critique atteint au jour {tc} ") 
else: 
print(" Aucun dépassement du seuil critique Imax détecté.") 
plt.xlabel("Jour") 
plt.ylabel("Infectés actifs") 
plt.title("Temps critique pour une intervention sanitaire") 
plt.legend() 
plt.grid(True) 
plt.tight_layout() 
plt.show()
