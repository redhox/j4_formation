import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
from geopy.geocoders import Nominatim
import geopy.exc

# Coordonnées des 4 sites de l'entreprise de plomberie
coordo_sites = np.array([
    [4.56749177e01, -4.79134161e-01],  # Site N°1
    [4.79013224e01, 5.96212449e00],   # Site N°2
    [4.90197399e01, 2.15708360e00],   # Site N°3
    [4.41086654e01, 4.72918709e00]    # Site N°4
])

# Demander à l'utilisateur d'entrer une adresse
adresse = st.text_input("Entrez votre adresse postale")

# Convertir l'adresse en coordonnées
if adresse:
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(adresse)
        coordo_client = np.array([location.latitude, location.longitude])
        st.write(f"Coordonnées du client : {coordo_client}")

        # Calculer la distance euclidienne entre les coordonnées du client et celles de chaque site en utilisant une formule appropriée.
        # Distance euclidienne = racine((x_site - x_client)² + (y_site - y_client)²)
        distances = []
        for coordo_site in coordo_sites:
            distance = np.sqrt((coordo_site[0] - coordo_client[0]) ** 2 + (coordo_site[1] - coordo_client[1]) ** 2)
            distances.append(distance)

        distances = np.array(distances)

        # Identifier la distance minimale parmi les distances calculée
        indice_site_plus_proche = np.argmin(distances)

        # Déterminer le site correspondant à la distance minimale comme étant le site le plus proche du client
        site_plus_proche = f"Site N°{indice_site_plus_proche + 1}"
        st.title(f"Le site le plus proche du client est le {site_plus_proche}")


        # Créer une carte interactive
        m = folium.Map(location=[coordo_client[0], coordo_client[1]], zoom_start=10)

        # Ajouter les marqueurs pour les sites
        for i, coordo_site in enumerate(coordo_sites):
            folium.Marker(location=[coordo_site[0], coordo_site[1]], popup=f"Site N°{i + 1}").add_to(m)

        # Ajouter le marqueur pour le client
        folium.Marker(location=[coordo_client[0], coordo_client[1]], popup="Client").add_to(m)

        # Afficher la carte avec st.map()
        folium_static(m)

    except (AttributeError, geopy.exc.GeocoderTimedOut, geopy.exc.GeocoderUnavailable):
        st.write("Adresse invalide. Veuillez entrer une adresse valide.")


# Considérons deux points p' et p de coordonnées respectives (x', y') et (x ,y )
# Leur distance euclidienne est donnée par la formule ||p'−p|| = √ (x' − x )² + (y' − y )²