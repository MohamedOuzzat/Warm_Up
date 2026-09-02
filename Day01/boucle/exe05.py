"""
Écrivez un programme Python qui demande à l'utilisateur de saisir une chaîne de caractères, puis
affiche cette chaîne inversée.
"""

chaine = input("chaine : ")

print(len(chaine))
nov_chaine = ""

for i in reversed(chaine):
    nov_chaine+=i

print(nov_chaine)