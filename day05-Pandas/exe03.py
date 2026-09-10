import pandas as pd
import numpy as np

df = pd.read_csv('file/inscri.csv')
# print(reader)

# 1. Identifier les problèmes présents dans le dataset.


# 2. Rechercher les valeurs manquantes.
# print(df[df.isnull()])

# 3. Identifier les doublons.
# print(df[df.duplicated()])

# 4. Supprimer les doublons.
# print(df.drop_duplicates())

# 5. Nettoyer les espaces dans les noms.
df['nom'].str.replace(' ', '')
# print(df['nom'])

# 6. Nettoyer les espaces dans les villes.
df['ville'].str.replace(' ', '')
print(df['ville'])

# 7. Standardiser les noms des villes.
# 8. Transformer `"N/A"` en valeur manquante.
df['age'] = df['age'].replace('N/A', np.nan)
# 9. Convertir `age` en numérique.
df['age']=df['age'].replace(np.nan,20)
# print(df)

# 10. Nettoyer la colonne `salaire`.
df['salaire']=df['salaire'].replace('4500 DH',4500)
print(df)

# 11. Supprimer `"DH"` de la colonne salaire.
# 12. Transformer `salaire` en numérique.
# 13. Identifier le salaire négatif.
negatif=df['salaire']<0

# 14. Traiter cette valeur invalide avec une stratégie pertinente.
# 15. Transformer `date_inscription` en datetime.
# 16. Vérifier les types finaux.
# 17. Vérifier le nombre de lignes après nettoyage.
# 18. Vérifier que le dataset final est cohérent.