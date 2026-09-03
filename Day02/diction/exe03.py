notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12}

print(notes.keys())
print(notes.values())
print(notes.items())
count=0
for key,value in notes.items():
    
        count+=value

moyenne = count / len(notes)
print(count)
print(moyenne)