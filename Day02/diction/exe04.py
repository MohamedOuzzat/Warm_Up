notes_etudiants = {"Omar": 15, "Sara": 8, "Yassine": 17, "Imane": 11, "Hamza": 6, "Nadia":
14}

note_sup={}
note_inf={}
for key,value in notes_etudiants.items():
    if value >= 10:
        note_sup={
            key:value
        }
        # del notes_etudiants[value]
    elif value<10:
        note_inf={
            key:value
        }
        # notes_etudiants.popitem(value)
    else:
        continue

print(notes_etudiants)
print(note_inf)
print(note_sup)


# for key,value in notes_etudiants.items():


