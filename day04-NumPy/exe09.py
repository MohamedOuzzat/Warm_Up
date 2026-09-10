import numpy as np
ventes=np.array([
                [123,213,4564,564,234],
                [3544,645,546,896,8690],
                [2932,345,9078,5345,8678]
                ])

"""Calculer : les ventes totales et moyennes par produit, 
les ventes totales et moyennes par mois, ainsi que le
meilleur produit et le meilleur mois."""
v_total_produit=ventes.sum(axis=0)
moyenne_produit=ventes.mean(axis=0)
v_total_mois=ventes.sum(axis=1)
moyenne_mois=ventes.mean(axis=1)

meilleur_produit=ventes.max(axis=0)
meilleur_mois=ventes.max(axis=1)

print(f"les ventes totales par produit{v_total_produit}")
print(f"le moyennes par produit {moyenne_produit}")
print(f"les ventes totales par mois {v_total_mois}")
print(f"le moyennes par mois {moyenne_mois}")
print(f"le meilleur produit {meilleur_produit}")
print(f"le meilleur mois {meilleur_mois}")

print(ventes.shape)
