
"""
Écrivez un programme Python qui demande le nom d'un employé, son salaire horaire et le nombre
d'heures travaillées.
Calculez son salaire total en considérant que les heures travaillées au-delà de 40 heures sont
rémunérées à 1,5 fois le salaire horaire.
Affichez le salaire total de l'employé.
"""

nom = str(input("nom : "))
salaire = float(input("salaire : "))

h_tr = int(input("heures travaillées : "))

if h_tr > 40:
    plus=h_tr - 40
    count = plus * 1.5
    total = salaire * h_tr + count
    print(f"total : {total}")

else:
    total = salaire * h_tr 
    print(f"total : {total}")
