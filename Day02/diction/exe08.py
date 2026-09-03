"""
CALCULS DEMANDÉS
Nombre total de ventes & Chiffre d'affaires (CA) total.
Produit le plus cher & Quantité totale vendue.
Chiffre d'affaires par produit & Nombre de produits par catégorie.
 Processus Analyste : Données brutes ➔ Parcours ➔ Transformation ➔ Agrégation ➔ Résultats

"""
ventes = [
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 2},
 {"produit": "Souris", "categorie": "Accessoire", "prix": 150, "quantite": 10},
 {"produit": "Clavier", "categorie": "Accessoire", "prix": 300, "quantite": 5},
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 1},
 {"produit": "Écran", "categorie": "Informatique", "prix": 2500, "quantite": 3}
]

print(f"Nombre total de ventes : {len(ventes)}")

count=0
for ele in ventes:
    count+=ele["quantite"]*ele["prix"]

print(count)

maxPricedItem = max(ventes, key=lambda x:x['prix'])
print(maxPricedItem)

# for ele in ventes:
#    for key,value in ele.items():
#        if key=="prix":
#            print(max(ele["prix"]))
