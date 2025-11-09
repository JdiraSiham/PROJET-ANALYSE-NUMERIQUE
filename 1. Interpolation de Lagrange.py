def interpolation_lagrange(jour, data, x):  
    total = 0.0 
    n = len(jour) 
    for i in range(n): 
        terme = data[i] 
        for j in range(n): 
            if j != i: 
                terme *= (x - jour[j]) / (jour[i] - jour[j]) 
        total += terme 
    return total 
 
# Données complètes 
jours = [ 
    1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141,  
    151, 161, 171, 181, 191, 201, 211, 221, 231, 241, 251, 261, 271, 281,  
    291, 301, 311, 321, 331, 341, 351, 361, 371, 381, 391, 401, 411, 421,  
    431, 441, 451, 461, 471, 481, 491, 500] 
 
infectes = [ 
    1, 5, 86, 617, 1431, 3209, 4423, 6063, 7133, 7780, 
    8437, 9613, 12248, 14771, 17236, 20278, 27217, 38805, 58489,  
    72394, 94504, 119107, 140024, 173632, 203733, 246349, 293177,  
    340684, 376738, 406970, 430562, 443146, 456334, 469139, 478135,  
    480056, 482994, 485974, 488632, 491463, 494659, 497832, 500948,  
    504260, 507938, 511562, 515023, 518868, 522765, 526651, 566356] 
retablis = [ 
    0, 1, 3, 24, 105, 393, 984, 2554, 4098, 5401, 7493, 8117, 8740,  
    11316, 14921, 16438, 19629, 26687, 43049, 55274, 74930, 97468,  
    118142, 143972, 168706, 202491, 238276, 289808, 327693, 365036,  
    396276, 415829, 431167, 445250, 456032, 463271, 468387, 470425,  
    472991, 475911, 482352, 484793, 487414, 490366, 493873, 497382,  
    503483, 507681, 511842, 513681, 536626] 
deces=[ 
    0, 1, 3, 36, 105, 145, 170, 188, 194, 204, 210, 213, 224, 242,  
    273, 313, 417, 584, 1052, 1361, 1714, 2113, 2439, 2928, 3445,  
    4079, 4829, 5619, 6184, 6740, 7240, 7485, 7784, 8224, 8466, 8540,  
    8608, 8653, 8693, 8745, 8798, 8842, 8882, 8940, 9000, 9060, 9104,  
    9160, 9220, 9238, 9498 
] 
 
# Points de test 
jours_test_intervalle = [8, 44, 76, 103, 128, 149, 178, 194, 208, 234, 263, 277, 304, 318, 
344, 368, 386, 399, 416, 448] 
jours_test_hors_intervalle = [502, 534, 558, 576, 608, 623, 647, 662, 684, 706, 728, 749, 772, 
793, 814, 836, 857, 878, 892, 908] 
jours_test_reference = [21, 31, 51, 71, 101, 111, 141, 161, 181, 201, 251, 281, 321, 331, 371, 
391, 411, 431, 461, 491] 
print("\n VALEURS DANS L'INTERVALLE ") 
for jour in jours_test_intervalle: 
    I = interpolation_lagrange(jours, infectes, jour) 
    R = interpolation_lagrange(jours, retablis, jour) 
    D = interpolation_lagrange(jours, deces, jour) 
    print(f"Jour : {jour}") 
    print("Valeur estimée avec Lagrange :") 
    print(f"  Cas infectés (I) : {I:.2f}") 
    print(f"  Cas rétablis (R) : {R:.2f}") 
    print(f"  Cas décédés (D)  : {D:.2f}") 
 
print("\n VALEURS HORS INTERVALLE ") 
for jour in jours_test_hors_intervalle: 
    I = interpolation_lagrange(jours, infectes, jour) 
    R = interpolation_lagrange(jours, retablis, jour) 
    D = interpolation_lagrange(jours, deces, jour) 
    print(f"Jour : {jour}") 
    print("Valeur estimée avec Lagrange :") 
    print(f"  Cas infectés (I) : {I:.2f}") 
    print(f"  Cas rétablis (R) : {R:.2f}") 
    print(f"  Cas décédés (D)  : {D:.2f}") 
     
 
print("\n VALEURS DE RÉFÉRENCE ") 
for jour in jours_test_reference: 
    I = interpolation_lagrange(jours, infectes, jour) 
    R = interpolation_lagrange(jours, retablis, jour) 
    D = interpolation_lagrange(jours, deces, jour) 
    print(f"Jour : {jour}")    print("Valeur estimée avec Lagrange :") 
    print(f"  Cas infectés (I) : {I:.2f}") 
    print(f"  Cas rétablis (R) : {R:.2f}") 
    print(f"  Cas décédés (D)  : {D:.2f}") 
