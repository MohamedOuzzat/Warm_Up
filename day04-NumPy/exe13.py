import numpy as np

array=np.array([
                [12,32,11,np.nan,382,123,np.nan],
                [-21,np.nan,np.nan,940,-23,np.nan,90],
               
               ])

pos= array<0 
Non=np.isnan(array)
gra=array>100

result=pos|Non|gra
# print(result)
new_arr = array[~result]

# print(array[result])

print(new_arr)