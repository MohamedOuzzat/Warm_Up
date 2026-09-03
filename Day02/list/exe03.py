"""
Afficher toutes les notes.
Calculer la moyenne.
Créer une liste contenant les notes supérieures à la moyenne.
Créer une liste contenant les notes inférieures à la moyenne.
Trouver la meilleure note et la plus mauvaise note.
Compter le nombre de notes supérieures ou égales à 10 et calculer le pourcentage de réussite.

Formule : (Nombre de réussites ÷ Nombre total de tentatives) × 100

"""
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]


print(notes)
count = sum(notes)
moyenne=count/(len(notes))
print(moyenne)

sup_list=[]

for n in notes:
    if n > moyenne:
        sup_list.append(n)

print(sup_list)

inf_list = []

for n in notes:
    if n < moyenne:
        inf_list.append(n)


print(max(notes))

print(min(notes))

# Compter le nombre de notes supérieures ou égales à 10 et calculer le pourcentage de réussite.
count=0
for n in notes:
    if n >= 10:
        count+=1
calcul = int (count/(len(notes)) * 100)
        

print(calcul)