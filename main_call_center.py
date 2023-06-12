import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

# Charger les données
my_data = pd.read_excel("Databases/Appels.xlsx")
my_data = np.array(my_data)

# Créer les variables
n = len(my_data)
t = np.zeros(n)
t[0] = my_data[0, 0]
for i in range(1, n):
    t[i] = my_data[i, 0] - my_data[i - 1, 0]
t = t / 60
t = np.array(t, dtype=int)
t = t.reshape(-1, 1)
x = my_data[:, 1].reshape(-1, 1)

# Créer le modèle
from sklearn import LinearRegression
model = LinearRegression()
model.fit(t, x)

# Prédire le nombre d'appels
t_pred = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]).reshape(-1, 1)
x_pred = model.predict(t_pred)
x_pred = np.array(x_pred, dtype=int)
print(x_pred)

# Afficher le graphique
import matplotlib.pyplot as plt
plt.scatter(t, x, color='red')
plt.plot(t_pred, x_pred, color='blue')
plt.title('Appels par minute')
plt.xlabel('Temps (minutes)')
plt.ylabel('Nombre d\'appels')
plt.show()

# Afficher le coefficient de détermination
print(model.score(t, x))

# Afficher les coefficients
print(model.coef_)
print(model.intercept_)

