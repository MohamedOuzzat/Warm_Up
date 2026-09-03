"""
TRAVAIL À FAIRE
Afficher la liste originale, puis créer une copie ( copy() ).
Trier la première copie dans l'ordre croissant et une deuxième copie dans l'ordre décroissant.
Afficher les deux résultats ainsi que les trois meilleurs scores.
 Attention : scores.copy() != scores et sort() modifie la liste sur place ! 
 """

scores = [45, 12, 78, 34, 90, 23, 67, 56, 89, 10]

print(scores)
S_copy=scores.copy()
S_copy_2=scores.copy()

print(S_copy)
S_copy.sort()

print(S_copy)
S_copy_2.sort(reverse=True)

print(S_copy_2)

print(S_copy_2[0:3])