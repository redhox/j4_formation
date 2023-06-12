import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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
#1
my_data = pd.read_excel("../DDB/Recette.xlsx")
total = my_data.apply(lambda x: x['Prix'] * x['Quantite'], axis=1).sum()
print("le total de la recette vendue= ",total)

#2
my_data = pd.read_excel("../DDB/Recette.xlsx")
total_by_day = my_data.groupby('Jour').apply(lambda x: (x['Prix'] * x['Quantite']).sum()).reset_index(name='Total')
print(total_by_day)

#3
filtered_data = my_data[my_data['Quantite'] > 0]
unique_products = filtered_data['Produits Laitiers'].drop_duplicates()
print(unique_products)

#4
# Regroupement par produit laitier et somme des quantités
quantites_par_produit = filtered_data.groupby('Produits Laitiers')['Quantite'].sum()
print(quantites_par_produit)

#5
product_quantities = my_data.groupby('Produits Laitiers')['Quantite'].sum()

# Tracé de l'histogramme
fig, ax = plt.subplots()
ax.bar(product_quantities.index, product_quantities.values)
plt.xticks(rotation=90)
ax.set_xlabel('Produit')
ax.set_ylabel('Quantite')
ax.set_title('Histogramme de la quantité vendue de chaque produit')
st.pyplot(fig)

#6
my_data['Prix_total'] = my_data['Prix'] * my_data['Quantite']
resultats_par_produit = my_data.groupby('Produits Laitiers')['Prix_total'].sum()
print(resultats_par_produit)

#7
# Utiliser groupby() pour regrouper les données par produit et trouver le prix maximum et minimum de chaque groupe
max_prices = my_data.groupby('Produits Laitiers')['Prix'].max()
min_prices = my_data.groupby('Produits Laitiers')['Prix'].min()

# Afficher les résultats
print("Prix maximaux :")
print(max_prices)
print("Prix minimaux :")
print(min_prices)

#8
total = my_data['Reduction'].sum()

# Afficher le résultat
print("La somme des reduction est : ", total)
