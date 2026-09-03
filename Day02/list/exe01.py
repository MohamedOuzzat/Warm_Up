"""
A. Accéder aux données
Afficher la liste complète.
Afficher le premier élément.
Afficher le dernier élément.
Afficher le troisième élément.
B. Utiliser le slicing
Afficher les trois premiers éléments.
Afficher les trois derniers éléments.
Afficher un élément sur deux.

C. Modifier les données
Remplacer "Orange" par "Ananas" .
Afficher la liste après modification.

"""


fruits = ["Pomme", "Banane", "Orange", "Fraise", "Mangue", "Kiwi","kokok", "Fraise", "Mangue", "Kiwi", "Fraise", "Mangue", "Kiwi", "Fraise", "Mangue", "Kiwi"]

# Afficher la liste complète.
print(fruits)
# Afficher le premier élément.
print(fruits[0])
# Afficher le dernier élément.
print(fruits[len(fruits)-1])
print(fruits[:-1])
# Afficher le troisième élément.
print(fruits[2])

# Afficher les trois premiers éléments.
print(fruits[0:3])

# Afficher les trois derniers éléments.
print(fruits[-3::])


# Afficher un élément sur deux.
print(fruits[::2])


x=fruits.index("Orange")
fruits[x]="Ananas"

# Afficher la liste après modification.
print(fruits)

