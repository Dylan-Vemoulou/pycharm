1# Séparation du CSV + rename de la colonne

import pandas as pd
df = pd.read_csv('RA.csv', sep =';')
df = df.rename(columns={'Unnamed: 0': 'code-postal'})
df


2# Afficher le contenu de chaque ligne
for i, row in df.iterrows():
    print(row)


3# Afficher le nom des départements ou les graminées > 0
for i, row in df.iterrows():
    graminees = row.loc['graminees']
    if graminees > 0:
        departements = row.loc['departements']
        print(departements)

4# Afficher le nom des départements ou les graminées > 0 similaire au code du dessus mais en 1 ligne

df1 = df.loc[df['graminees'] > 0]
print(df1)


5# Afficher le ou les noms de départements ou les niveau des graminnées et ambroisies est = 0
for i, row in df.iterrows():
    graminees = row.loc['graminees']
    ambroisies = row.loc['ambroisies']
    if (graminees and ambroisies) < 1:
        departements = row.loc['departements']
        print(departements)

6# Afficher le ou les noms de départements ou les niveau des graminnées et ambroisies est = 0 en 1 ligne

        df2 = df.loc[df['graminees'] < 1]
        df2 = df.loc[df['ambroisies'] < 1]
        print(df2)


7# Coupler les départements ou le niveau de graminees et ambroisies est identique

for i, row in df.iterrows():
    graminees = row.loc['graminees']
    ambroisies = row.loc['ambroisies']
    departements = row.loc['departements']
    print("-----------------------------------")
    print(departements)
    for j, row1 in df.iterrows():
        graminees1 = row1.loc['graminees']
        ambroisies1 = row1.loc['ambroisies']
        departements1 = row1.loc['departements']

        if graminees == graminees1:
            if ambroisies == ambroisies1:
                print(departements1)


8# Classer dans l'ordre décroissant le niveau des départements en fonction du graminees

print(df.sort_values(by=['graminees'],ascending=False))
print(df)

9# Moyenne du niveau de risque de chaque départements

dfmoyenne = df.mean(axis=1)
print(dfmoyenne)

#Colonne
dfmoy = df.mean()
print(dfmoy)

10# Déterminer la valeur médiane

mediane = df.median()
print("La veleur médiane est : ")
print(mediane)

11# Déterminer le minimum et le maximum

dfmin = df['graminees'].min()
print(dfmin)

dfmax = df['graminees'].max()
print(dfmax)

12# Indice du min et max
dfimax = df['graminees'].idxmax()
print(dfimax)

dfimin = df['graminees'].idxmin()
print(dfimin)

