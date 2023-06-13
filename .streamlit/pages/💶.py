import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

"""
5. Tracer un histogramme de la quantité vendue de chaque produit.

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
