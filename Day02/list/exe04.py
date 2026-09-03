"""
Créer une liste des températures > 25.
Créer une liste des températures ≤ 25.
Créer une liste des températures comprises entre 20 et 30 inclus (remarque : 20 <= temp <= 30 ).
Compter le nombre de températures supérieures à 30.
"""
temperatures = [18, 25, 31, 14, 27, 35, 22, 19, 30, 12, 28]
te_sup_25 =[]
te_inf=[]
te_comprises=[]
te_sup_30=[]
count=0
for t in temperatures:
    if t > 25:
        te_sup_25.append(t)
for t in temperatures:
    if t <= 25:
        te_inf.append(t)
for t in temperatures:
    if t >= 20 and t <= 30:
        te_comprises.append(t)

for t in temperatures:
    if t > 30:
       count+=1
       

print(count)
        
