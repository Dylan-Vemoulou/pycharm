# Pycharm 

 Qu'est ce que c'est ? 

C'est un environnement de développement intégré utiliser pour programmer en python

  • Il permet l'analyse de code et contient un débogueur graphique.
  
  • Il permet également la gestion des tests unitaires c'est à dire qu'on peux exécuter les parties du code ligne par ligne

  • C'est ainsi un excellent outil de programmation.

 Les caractéristiques de Pycharm 
  
    
    Pycharm est livré avec une console python où vous pouvez écrire les scripts pendant que vous les exécutez. Les fenêtres peuvent être commutées en mode dock, en mode fenêtre     ou encore en mode fractionné selon le goût et l'aisance de chacun.
    Il aide aide au codage et à l'analyse avec la complétion de code et l'analyse des erreurs et de la syntaxe.
    
    Les exercices Pycharm
    
    Après m'être renseigné sur cet environnement, je me suis exercer pour mieux me familiariser avec Pycharm.
    
    J'ai participé à différents exercices.
    
      Je vais afficher les différents codes qui m'ont permis de réussir les exercices.
      
      Dans les différents qui suivent, je devais établir des codes en ayant un fichier csv (fichier informatique de type tableur) avec donc différentes données.
      
        1) Séparer les différentes colonnes du CSV et rename la première colonne en "Code Postal"
        
          Voici le code : 
          
            # Séparation du CSV + rename de la colonne

              import pandas as pd
              df = pd.read_csv('RA.csv', sep =';')
              df = df.rename(columns={'Unnamed: 0': 'code-postal'})
              df

        2) Afficher le contenu de chaque ligne 
        
        for i, row in df.iterrows():
        print(row)
  
  
        3) Afficher le nom des départements ou les graminées sont supérieur à 0
        
        for i, row in df.iterrows():
          graminees = row.loc['graminees']
          if graminees > 0:
            departements = row.loc['departements']
            print(departements)
            
         4) Même exercice mais sans utiliser de boucle for 
         
         df1 = df.loc[df['graminees'] > 0]
         print(df1)
         
         5) Afficher le ou les nom des départements ou les ambroisies et les graminées sont égales à 0
         
         for i, row in df.iterrows():
           graminees = row.loc['graminees']
           ambroisies = row.loc['ambroisies']
           if (graminees and ambroisies) < 1:
            departements = row.loc['departements']
            print(departements)
            
          6) Même exercice sans utiliser de boucle for 
          
          df2 = df.loc[df['graminees'] < 1]
          df2 = df.loc[df['ambroisies'] < 1]
          print(df2)
          
          7) Coupler les départements ou les niveaux des graminées et des ambroisies est identique 
          
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
              
           8) Classer dans l'ordre décroissant le niveau des départements en fonction des graminées 
           
           print(df.sort_values(by=['graminees'],ascending=False))
           print(df)
         
           9) Faire la moyenne du niveau de risques de chaques départements 
           
           dfmoyenne = df.mean(axis=1)
           print(dfmoyenne)
           
           10) Déterminer le minimum et le maximum de la colonne graminées
           
              Le minimum 
              
              dfmin = df['graminees'].max()
              print(dfmin)
              
              Le maximum 
              
              dfmax = df['graminees'].max()
              print(dfmax)
