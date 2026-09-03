etudiants = [
 {"nom": "Omar", "age": 22, "note": 15},
 {"nom": "Sara", "age": 21, "note": 17},
 {"nom": "Yassine", "age": 23, "note": 9},
 {"nom": "Imane", "age": 20, "note": 13},
 {"nom": "Hamza", "age": 24, "note": 7}
]
# Afficher les étudiants admis/échec, la moyenne de classe et l'étudiant ayant la meilleure note.
count=0
for ele in etudiants:
    count += ele["note"]


moyenne = count/len(etudiants)
        
print(count)
print(moyenne)

maxi=[]
maxV={}

print("les etudiants admin :")
for ele in etudiants:
     if ele["note"]>=10:
          print(ele)


print("les etudiants no admin :")
for ele in etudiants:
     if ele["note"]<10:
          print(ele)



        
maxNote = max(etudiants, key=lambda x:x['note'])

print(maxNote)

# for ele in etudiants:
#      for key,value in ele.items():
#       print(max(ele["note"]))