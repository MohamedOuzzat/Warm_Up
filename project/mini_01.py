"""
Objectif : Développer plusieurs petites fonctions indépendantes, chacune ciblant une compétence précise
Travail à faire :
Demander à l’utilisateur de saisir un nombre entier n et afficher la factorielle de ce nombre ( n! ).
Demander à l’utilisateur un nombre entier m et afficher sa table de multiplication de 1 à 10.
Demander à l’utilisateur un nombre entier L et indiquer s’il s’agit d’un carré parfait.
Demander une chaîne de caractères à l’utilisateur, puis afficher chaque caractère un par un.
Demander une phrase à l’utilisateur et afficher le mot le plus long de cette phrase.
Demander une chaîne de caractères Ch et afficher le nombre d’occurrences de chaque caractère.
Exemple : Pour Ch = “artificial intelligence developer”
Le programme doit afficher : Le caractère "i" figure 5 fois dans la chaîne Ch
"""
import math
def factorielle():
    count=1
    n=int(input("saisir un nombre entier : "))
    for i in range(1,n+1):
        
        count*=i
        
    print(f"factorielle de nombre {n} est : {count}")
    return count

factorielle()

def multiplication(n):
    for i in range(11):
        result=n*i
        print(f"{n} X {i} = {result}")

nombre=int(input(" entre  le nombre : "))
multiplication(nombre)

def parfait(L):

    result = math.sqrt(L)
    if type(result)==int:
        print(f"le nombre {L} est un carré parfait")
    else:
        print(f"le nombre {L} n'est pas un carré parfait")

n=int(input("entrez un nombre : "))
parfait(n)



def chaine(c):
    for i in range(len(c)):
        print(c[i])

ch=input("entrez un chaine de character : ")
chaine(ch)


def plus_lange(ph):
    maxI=""
    chaine=ph.split(" ")
    for i in chaine:
        if len(i) > len(maxI):
            maxI=i
        else:
            continue
    print(f"mot le plus long de : {maxI}")

phrase= input("phrase : ")
plus_lange(phrase)


def occurrences(c):
    ch=[]
    for i in c:
        if i in ch:
            continue
            
        else:
            ch.append(i)
            print(f"Le caractère {i} figure {c.count(i)} fois dans la chaîne")
            


chaine= input("chaine de character : ")
occurrences(chaine)

