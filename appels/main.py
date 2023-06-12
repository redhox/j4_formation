import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt


my_data = pd.read_excel("Databases/Appels.xlsx")

# Calculer la durée totale des appels en format hh:mm:ss
total_duration = my_data['hh'].sum()*3600 + my_data['mm'].sum()*60 + my_data['ss'].sum()
hours = total_duration // 3600
minutes = (total_duration % 3600) // 60
seconds = total_duration % 60
formatted_duration = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
print("Durée totale des appels :", formatted_duration)

# Lister les numéros des appels entrants
incoming_calls = my_data[my_data['En_Sor'] == 'En']['Numéro']
print("Numéros des appels entrants :", list(incoming_calls))

# Lister les numéros des appels sortants
outgoing_calls = my_data[my_data['En_Sor'] == 'Sor']['Numéro']
print("Numéros des appels sortants :", list(outgoing_calls))

# Calculer la durée totale des appels entrants en format hh:mm:ss
incoming_duration = my_data[my_data['En_Sor'] == 'En'][['hh', 'mm', 'ss']].sum()
incoming_hours = incoming_duration['hh'] + (incoming_duration['mm'] + incoming_duration['ss'] // 60) // 60
incoming_minutes = (incoming_duration['mm'] + incoming_duration['ss'] // 60) % 60
incoming_seconds = incoming_duration['ss'] % 60
formatted_incoming_duration = f"{incoming_hours:02d}:{incoming_minutes:02d}:{incoming_seconds:02d}"
print("Durée totale des appels entrants :", formatted_incoming_duration)

# Calculer la durée totale des appels sortants en format hh:mm:ss
outgoing_duration = my_data[my_data['En_Sor'] == 'Sor'][['hh', 'mm', 'ss']].sum()
outgoing_hours = outgoing_duration['hh'] + (outgoing_duration['mm'] + outgoing_duration['ss'] // 60) // 60
outgoing_minutes = (outgoing_duration['mm'] + outgoing_duration['ss'] // 60) % 60
outgoing_seconds = outgoing_duration['ss'] % 60
formatted_outgoing_duration = f"{outgoing_hours:02d}:{outgoing_minutes:02d}:{outgoing_seconds:02d}"
print("Durée totale des appels sortants :", formatted_outgoing_duration)

# Trouver le numéro avec la durée d'appel la plus longue
longest_duration = my_data[['Numéro', 'hh', 'mm', 'ss']].groupby('Numéro').sum().idxmax()
print("Numéro avec la durée d'appel la plus longue :", longest_duration[0])
