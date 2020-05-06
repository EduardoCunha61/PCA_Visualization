import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
#matplotlib inline

db = pd.read_csv("lipids.csv") #Name of file
df = db.drop(db.columns[0], axis=1)

scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

pca = PCA(n_components=2)
pca.fit(scaled_data)
aux = pca.transform(scaled_data)
df_pca = pd.DataFrame(data = aux, columns = ['principal component 1', 'principal component 2'])

final_pca = pd.concat([df_pca, db['type']], axis = 1)
print(final_pca)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 11)
ax.set_ylabel('Principal Component 2', fontsize = 11)
types = ['CP','NC'] 
colors = ['r', 'b']
for t, color in zip(types,colors):
    indicesToKeep = final_pca['type'] == t
    ax.scatter(final_pca.loc[indicesToKeep, 'principal component 1']
               , final_pca.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)

ax.legend(types)
ax.grid()

fig = ax.get_figure()
fig.savefig("lipids.png") #Name of picture with pca