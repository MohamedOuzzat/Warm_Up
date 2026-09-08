import numpy as np
salaires =np.array([1222,3212,3212,4323,1289])
# Calculer : moyenne, médiane, variance, écart-type, minimum, maximum, ainsi que le 1er et 3ème quartiles.
print(f"moyenne : {salaires.mean()}")
print(f"médiane : {np.median(salaires)}")
print(f"variance : {np.var(salaires)}")
print(f"écart-type : {np.std(salaires)}")
print(f"minimum : {salaires.min()}")
print(f"maximum : {salaires.max()}")
print(salaires[0:2])
print(f"le porcentage 50% : {np.percentile(salaires,50)}")