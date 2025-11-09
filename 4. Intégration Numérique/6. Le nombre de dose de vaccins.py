# Paramètres 
N = 36000000 
a = 0.014 
b = 0.0040108 
r = 0.04108 
# Calcul de R0 
R0 = r / (a + b) 
# Seuil d'immunité collective 
seuil = 1 - 1/R0 
# Nombre de personnes à vacciner 
vaccins_necessaires = seuil * N 
print("R0 estimé :", round(R0, 2)) 
print("Seuil d'immunité collective :", round(seuil * 100, 2), "%") 
print("Nombre de personnes à vacciner :", int(vaccins_necessaires)) 
