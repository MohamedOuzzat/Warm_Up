"""
La suite de Syracuse (aussi appelée suite de Collatz ou conjecture de Syracuse) est une suite définie pour un entier naturel positif n comme suit :

Si n est pair, le terme suivant est n // 2.

Si n est impair, le terme suivant est 3n + 1.

La suite se termine lorsque n devient égal à 1.

Écrire un code permettant de calculer cette suite
"""

nombre = int(input("nombre : "))

while nombre!=1:
    if nombre % 2 ==0:
     nombre = nombre // 2
    
    else:
        nombre = (nombre * 3) + 1
    print(nombre)
