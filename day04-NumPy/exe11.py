import numpy as np 
capteurs_comportant=np.array([
                                -13,42.5,-654,2.13,-12,
                                35,-645,-123,5,344,
                                17.23,65.44,42,90.42,60.22

                                ]) 

P=capteurs_comportant>0
positive=np.where(capteurs_comportant > 0)
# integer=np.where(capteurs_comportant.dtype()==int)

print(P)
print(positive)
# print(integer)
# print(np.argwhere(positive)
print(capteurs_comportant[positive])
