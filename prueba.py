#-------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE, Isomap
from sklearn.decomposition import PCA
import umap

# Generación de dataframe a partir del CSV
df = pd.read_csv('1000_Companies.csv')

# Visualización de las primeras 5 filas para conocer la estructura de los datos
print(df.head())