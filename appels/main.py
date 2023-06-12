import numpy as np
import pandas as pd

# 1 - Charger les données à partir du fichier Excel
data = pd.read_excel('DDB/Appels.xlsx')
data = data.to_numpy()

# 2 - Calculer la durée totale des appels en format hh:mm:ss.
numeros = data[:, 0]
en_sor = data[:, 1]
heures = data[:, 2].astype(int)
minutes = data[:, 3].astype(int)
secondes = data[:, 4].astype(int)

total_h = np.sum(heures)
total_m = np.sum(minutes)
total_s = np.sum(secondes)

duree_totale_secondes = total_h * 3600 + total_m * 60 + total_s

h = int(duree_totale_secondes // 3600)
m = int((duree_totale_secondes % 3600) // 60)
s = int(duree_totale_secondes % 60)

print(f"Durée totale des appels : {h:02d}:{m:02d}:{s:02d}")

# 3 - Lister les numéros des appels entrants.
appels_entrants = np.unique(numeros[en_sor == 'En'])
for numero_entrant in appels_entrants:
    print("Numéros des appels entrants : ", numero_entrant)

# 4 - Lister les numéros des appels sortants.
appels_sortants = np.unique(numeros[en_sor == 'Sor'])
for numero_sortant in appels_sortants:
    print("Numéros des appels sortants : ", numero_sortant)

# 5 - Calculer la durée totale des appels entrants en format hh:mm:ss.
duree_entrants = np.sum((en_sor == 'En') * (secondes + minutes*60 + heures*3600))
heures_entrants = int(duree_entrants / 3600)
minutes_entrants = int((duree_entrants % 3600) / 60)
secondes_entrants = int((duree_entrants % 3600) % 60)
duree_formatee_entrants = f"{heures_entrants:02d}:{minutes_entrants:02d}:{secondes_entrants:02d}"
print("Durée totale des appels entrants : ", duree_formatee_entrants)

# 6 - Calculer la durée totale des appels sortants en format hh:mm:ss.
duree_sortants = np.sum((en_sor == 'Sor') * (secondes + minutes*60 + heures*3600))
heures_sortants = int(duree_sortants / 3600)
minutes_sortants = int((duree_sortants % 3600) / 60)
secondes_sortants = int((duree_sortants % 3600) % 60)
duree_formatee_sortants = f"{heures_sortants:02d}:{minutes_sortants:02d}:{secondes_sortants:02d}"
print("Durée totale des appels sortants : ", duree_formatee_sortants)

# Trouver le numéro avec la durée d'appel la plus longue.
index_duree_max = np.argmax(secondes + minutes*60 + heures*3600)
numero_duree_max = numeros[index_duree_max]
print("Numéro avec la durée d'appel la plus longue :", numero_duree_max)
