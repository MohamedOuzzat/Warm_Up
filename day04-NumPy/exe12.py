# np.nan 
import numpy as np

array=np.array([
                [12,32,11,np.nan,382,123,np.nan],
                [21,np.nan,np.nan,940,23,np.nan,90],
               
               ])

Nan=np.where(np.isnan(array))

# print(np.isnan(array))
# print(Nan)
moyenne = np.isnan(array).mean()
# print(np.argwhere(array[Nan]))

print(moyenne)
array[Nan]=[1,2,3,4,5]
print(array[Nan])
print(array)