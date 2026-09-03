"""
Challenge 2 : Produit
produit = {
 "nom": "Ordinateur", "prix": 8500,
 "stock": 12, "categorie":
"Informatique"
}
Modifier le prix à 7900.
Ajouter "marque": "Lenovo" et "disponible":
True .
Supprimer "stock" avec del et "categorie"
avec pop() .
"""
produit = {
 "nom": "Ordinateur", "prix": 8500,
 "stock": 12, "categorie":
"Informatique"
}

produit["prix"]=7900
produit["marque"]="Lenovo"
produit["disponible"]=True

del produit["stock"]

produit.pop("categorie")

print(produit)