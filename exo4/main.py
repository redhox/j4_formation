import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

file1 = open("../DDB/ADN_1.txt", "r")
file2 = open("../DDB/ADN_2.txt", "r")

#1
content1 = file1.read()
content2 = file2.read()
combined_content = content1 + content2
# Conversion de la chaîne de caractères en un tableau Numpy
characters = np.array(list(combined_content))
print(characters)

#2

with open('../DDB/ADN_1.txt', 'r') as f1, open('../DDB/ADN_2.txt', 'r') as f2:
    # Lire le contenu des fichiers
    contenu_fichier1 = f1.read()
    contenu_fichier2 = f2.read()
    # Calculer le nombre total de caractères
    nb_caracteres_total = len(contenu_fichier1) + len(contenu_fichier2)
    # Afficher le résultat
    print("Le nombre total de caractères est :", nb_caracteres_total)

#3
# Ouverture du fichier texte
unique_chars = np.unique(list(combined_content))

# Compter le nombre d'apparitions de chaque caractère dans la séquence
for char in unique_chars:
    count = combined_content.count(char)
    print(f"{char}: {count}")

#4
# Compter le nombre d'occurrences de chaque caractère unique
counts = np.unique(list(combined_content), return_counts=True)
# Calculer la proportion de chaque caractère
proportions = counts[1] / len(combined_content)
# Afficher les proportions
for i, char in enumerate(counts[0]):
    print(f"{char}: {proportions[i]}")