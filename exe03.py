"""
Un club privé souhaite contrôler l'accès à ses locaux selon certaines conditions. Une personne est
autorisée à entrer si :
• Elle a moins de 18 ans : l'entrée est refusée ;
• Elle a entre 18 et 25 ans : l'entrée est gratuite ;
• Elle a plus de 25 ans : l'entrée est autorisée uniquement si elle est membre du club ou
accompagnée d'un membre.
Écrivez un programme Python permettant d'afficher le message correspondant à la situation de la
personne.
"""
print("-----------Bonjour-----------")
nom = str(input("nom : "))
age = int(input("age : "))

if age < 18:
    print("l'entrée est refusée")

elif age >=18 and age <= 25:
    print("l'entrée est gratuite")
else:
    print(" l'entrée est autorisée uniquement si elle est membre du club ou accompagnée d'un membre.")