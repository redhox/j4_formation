import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
from geopy.geocoders import Nominatim
import geopy.exc

st.set_page_config(page_title="J4", page_icon ="🍻",layout="wide")
st.title("J4 - Morgan & Ibrahim")


# Considérons deux points p' et p de coordonnées respectives (x', y') et (x ,y )
# Leur distance euclidienne est donnée par la formule ||p'−p|| = √ (x' − x )² + (y' − y )²