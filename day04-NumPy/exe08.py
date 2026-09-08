import numpy as np
temperatures =np.array([[34,33,32,56,40],
                        [34,43,23,47,48],
                        [43,47,48,39,50],
                       ])

moyenne=temperatures.mean()

print(moyenne)
print(f" les jours les plus chauds {temperatures.max()}")
print(f" les jours les plus froids {temperatures.min()}")

sup=temperatures>moyenne
print(sup)
print(f"l'amplitude thermique : {temperatures.max()-temperatures.min()}")
print(f"les variations entre jours consécutifs : {np.diff(temperatures)}")