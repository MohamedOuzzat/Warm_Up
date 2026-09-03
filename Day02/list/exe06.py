"""
Objectif : Implémenter soi-même une recherche dans une liste sans utiliser list.index() .
Créer la fonction rechercheElement(element, liste) qui retourne l'indice si trouvé, sinon False .
"""
def rechercheElement(elemt,list):
    count=0
    for i in list:
        count+=1
        if i==elemt:
            print(count-1)
            break


N=[12,32,44,12,4,23,0]
rechercheElement(23,N)
