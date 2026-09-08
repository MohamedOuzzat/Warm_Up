import numpy as np
"""À partir d'un dataset (âge, salaire, ancienneté, dépenses), identifier : 
les clients > 30 ans, ceux au-dessus d'un
salaire donné, respectant plusieurs conditions simultanées ou non."""
clients = np.array([
                    [29,12000,4,233],
                    [40,40000,10,4432],
                    [36,30000,6,234],
                    [32,20000,5,546]
                    ])

sup_30=(clients>30).any(axis=0) 
# (clients is True)[3].any(axis=0)

print(sup_30)