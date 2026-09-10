import pandas as pd

df=pd.read_csv("file/data.csv")

# 1. Sélectionner la colonne `nom`.
print(df['nom'])

# 2. Sélectionner les colonnes `nom`, `age` et `ville`.
print(df[['nom','age','ville']])


# 3. Sélectionner les trois premières lignes avec `iloc`.
print(df.iloc[0:3,0:])

# 4. Sélectionner les clients ayant plus de 30 ans.
con=df['age']>30
print(df[con])

# 5. Sélectionner les clients ayant un salaire supérieur à 6 000.
sla_con=df['salaire']>6000
print(df[sla_con])

# 6. Sélectionner les clients de Casablanca.
casa_clients=df['ville']=='Casablanca'
print(df[casa_clients])

# 7. Sélectionner les femmes ayant plus de 30 ans.
femmes=df['sexe']=='F'
femmes_under=femmes & con
print(df[femmes_under])

# 8. Sélectionner les clients de Casablanca ou Rabat.
rabat_clients=df['ville']=='Rabat'
client_rabat_casa = rabat_clients | casa_clients
print(df[client_rabat_casa])

# 9. Utiliser `isin()` pour sélectionner plusieurs villes.

# print(df[df.isin({'ville': ['Rabat', 'Marrakech']})])
print(df['ville'].isin(['Rabat', 'Marrakech']))


# 10. Utiliser `between()` pour sélectionner les clients âgés de 25 à 35 ans.
filter_age= df[df["age"].between(25, 35)]
print(filter_age)

# 11. Utiliser `~` pour exclure une ville.
filter= df[~df["age"].between(25, 35)]

print(filter)

# 12. Extraire une cellule précise avec `loc` ou `iloc`.

# print(df['nom'].loc['s'])

# df.iloc[1] 
  # Returns Bob's row (index position 1)
