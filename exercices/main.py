import math
import numpy
import pandas
import streamlit as st
from streamlit_folium import folium_static
import folium
from geopy.geocoders import Nominatim
import geopy.exc

# Coordonnées des sites
coordo_sites = [
    (4.56749177e01, -4.79134161e-01),  # Site N°1
    (4.79013224e01, 5.96212449e00),  # Site N°2
    (4.90197399e01, 2.15708360e00),  # Site N°3
    (4.41086654e01, 4.72918709e00),  # Site N°4
]

# Demander à l'utilisateur d'entrer une adresse
adresse = st.text_input("Entrez votre adresse postale")

# Convertir l'adresse en coordonnées
if adresse:
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(adresse)
        coordo_client = (location.latitude, location.longitude)
        st.write(f"Coordonnées du client : {coordo_client}")

        # Calculer les distances entre le client et chaque site
        # Considérons deux points p' et p de coordonnées respectives (x', y') et (x ,y )
        # Leur distance euclidienne est donnée par la formule ||p'−p|| = √ (x' − x )² + (y' − y )²

        distances = [
            ((x - coordo_client[0]) ** 2 + (y - coordo_client[1]) ** 2) ** 0.5
            for x, y in coordo_sites
        ]

        # Trouver l'indice du site avec la distance minimale
        indice_site_plus_proche = distances.index(min(distances))

        # Déterminer le site correspondant à la distance minimale
        site_plus_proche = f"Site N°{indice_site_plus_proche + 1}"

        # Afficher le résultat
        st.title(f"Le site le plus proche du client est le {site_plus_proche}")

        # Créer une carte interactive
        m = folium.Map(location=[coordo_client[0], coordo_client[1]], zoom_start=10)

        # Ajouter les marqueurs pour les sites
        for i, coordo_site in enumerate(coordo_sites):
            folium.Marker(location=coordo_site, popup=f"Site N°{i + 1}").add_to(m)

        # Ajouter le marqueur pour le client
        folium.Marker(location=coordo_client, popup="Client").add_to(m)

        # Afficher la carte avec st.map()
        folium_static(m)

    except (AttributeError, geopy.exc.GeocoderTimedOut, geopy.exc.GeocoderUnavailable):
        st.write("Adresse invalide. Veuillez entrer une adresse valide.")


# # La méthode pour résoudre ce problème est la suivante :
# # Calculer la distance euclidienne entre les coordonnées du client et celles
# # de chaque site en utilisant une formule appropriée.
# # Identifier la distance minimale parmi les distances calculées.
# # Déterminer le site correspondant à la distance minimale comme étant le site le plus proche du client.
# # À l'aide de ces étapes, vous devez développer un code Python pour résoudre ce
# # problème spécifique de détermination du site le plus proche en utilisant les coordonnées GPS fournies.
