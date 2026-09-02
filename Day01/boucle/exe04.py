"""
Écrivez un programme Python qui demande à l'utilisateur de saisir un nombre entier N, puis calcule et
affiche la somme de tous les entiers compris entre 1 et N.
"""

N = int(input(" entrez un nombre : "))
total = 0
for i in range(1,N+1):
    total +=i
    print(i)

print(total)