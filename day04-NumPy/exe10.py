import numpy as np

clients = np.array([
                    [29,12000,4,1233],
                    [40,40000,10,123],
                    [36,30000,6,3842],
                    [3,20000,5,3238]
                    ])

sup_30 = (clients[:, 0] > 30)| (clients[:,-1]>2000)
print(clients[sup_30])
# (clients is True)[3].any(axis=0)

# print(sup_30)