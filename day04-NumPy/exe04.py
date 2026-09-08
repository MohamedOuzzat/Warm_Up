import numpy as np
# Créer un tableau représentant plusieurs clients avec : âge, revenu, nombre d'achats, montant dépensé.

client=np.array([
                [22,34,32,45],
                [12,22,14,1],
                [1,2,3,4],
                [122,340,123,442]
                ])

print(f"age : {client[0,3]}")
print(f"revenu : {client[1,3]}")
print(f"nombre d'achats : {client[2,3]}")
print(f"montant dépensé. : {client[3,3]}")