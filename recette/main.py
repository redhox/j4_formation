import numpy as np
import pandas as pd
"""
1. Calculer le total de la recette vendue.
2. Calculer la recette de chaque jour séparément.
3. Lister les produits vendus sans répétition.
4. Calculer la quantité vendue de chaque produit.
5. Tracer un histogramme de la quantité vendue de chaque produit.
6. Calculer la recette vendue de chaque produit séparément.
7. Trouver le prix le plus bas et le plus élevé pour chaque produit.
8. Calculer la somme totale des réductions appliquées.
9. Identifier le produit ayant bénéficié de la réduction la plus importante.
10. Calculer la moyenne des ventes pour chaque jour.
11. Calculer l'écart-type des ventes pour chaque jour.

    Jour  Produits Laitiers  Prix  Quantite  Reduction
0       1             Légume   1.2         1          0
1       1           Boissons   3.2         2         10
2       1  Produits Laitiers   4.6         1          5

"""

my_data = pd.read_excel("DDB/Recette.xlsx")
total = my_data.apply(lambda x: x['Prix'] * x['Quantite'], axis=1).sum()
print("le total de la recette vendue= ",total)


total_by_day = my_data.groupby('Jour').apply(lambda x: x['Prix'] * x['Quantite']).sum()
print(total_by_day)



