etudiant = {
 "nom": "Omar",
 "age": 22,
 "formation": {
                "nom": "Développement IA",
                "niveau": "Avancé", 
                "duree": 12
                }
}



etudiant["formation"]["niveau"]="Expert"
li=["Python", "SQL", "Pandas", "Machine Learning"] 

etudiant["technologies"]=li

print(etudiant)

# for key,value in etudiant.items():
#     for elemnt in value:
#         elemnt["niveau"]="Expert"


