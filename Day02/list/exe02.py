"""
A. Ajouter
Ajouter "PHP" à la fin.
Ajouter "SQL" à la fin.
Insérer "C" en deuxième position.

B. Supprimer & Analyser
Supprimer "Java" .
Supprimer le dernier élément.
Afficher la liste finale et le nombre d'éléments.


"""
langages = ["Python", "Java", "JavaScript", "C++"]

# Ajouter "PHP" à la fin.
langages.append("PHP")

# Ajouter "SQL" à la fin.
langages.append("SQL")

# Insérer "C" en deuxième position.
langages.insert(1,"C")

# Supprimer "Java" .
langages.remove("Java")

# Afficher la liste finale et le nombre d'éléments.
langages.pop()   

print(langages)