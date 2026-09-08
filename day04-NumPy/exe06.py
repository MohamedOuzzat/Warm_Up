import numpy as np
TVA=0.2
ventes = np.array([1212,4212,3123,4312,1233])

print(f"chiffre d'affaires(CA) : {np.sum(ventes)}")
print(f"TVA : {ventes*TVA}")
# le nombre de ventes, la vente moyenne, minimale et maximale.
print(f"le nombre de ventes : {ventes.size}")
print(f"la vente moyenne : {ventes.mean()}")
print(f"minimale : {ventes.min()}")
print(f"maximale : {ventes.max()}")