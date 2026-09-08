"""À partir d'un dataset client : modifier certaines valeurs, remplacer une
 ligne/colonne, extraire des lignes/
colonnes spécifiques, et créer une copie indépendante du dataset."""
import numpy as np
clients=np.array([
                [22,34,32,45],
                [12,22,14,1],
                [1,2,3,4],
                [122,340,123,442]
                ])

clients[2,3]=19
clients[2]=[12,13,14,15]

new_clients=clients.copy()

print(clients)
print(new_clients)