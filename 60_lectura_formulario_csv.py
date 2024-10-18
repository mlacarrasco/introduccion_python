"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias
 
 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.0 (08/11/2019)
 version 1.1 (20/12/2019)

    
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data/formulario_2023.csv')

print(data.columns)

feliz           = np.array(data[data.columns[1]])
sexo            = np.array(data[data.columns[2]])
score_python    = np.array(data[data.columns[3]])
horario         = np.array(data[data.columns[4]])
lenguaje        = np.array(data[data.columns[5]])
score_agotado   = np.array(data[data.columns[7]])
general_score   = np.array(data[data.columns[8]])


score_agotado =  score_agotado[:, np.newaxis]
general_score =  general_score[:, np.newaxis]


print("Promedio de datos reales: ")
print(data.columns[3],'promedio:', score_python.mean())
print(data.columns[7],'promedio:',score_agotado.mean())
print(data.columns[8],'promedio:',general_score.mean())

# graficamos los datos originales
fig, ax = plt.subplots(3,gridspec_kw={'hspace': 0.5}, figsize=(4,8))
ax[0].hist(x=score_python,bins=20,color='#8634eb',alpha=0.7,rwidth=0.95) 
ax[1].hist(x=sexo,bins=20,color='#8634eb',alpha=0.7,rwidth=0.95)
ax[2].hist(x=score_agotado,bins=20,color='#8634eb',alpha=0.7,rwidth=0.95)  
ax[0].set_title(data.columns[3])
ax[1].set_title(data.columns[2])
ax[2].set_title(data.columns[8])
plt.show()

