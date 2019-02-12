import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import Birch

data = pd.read_csv("winemag-data-130k-v2.csv")

variety_onehot = data['variety']
variety_onehot = pd.get_dummies(variety_onehot, columns = ['variety'], prefix = 'var')

variety_onehot.head()

province_onehot = data['province']
province_onehot = pd.get_dummies(province_onehot, columns = ['province'], prefix = 'prov')

province_onehot.head()

pca = PCA(n_components = 5, svd_solver = 'auto')

new_var = pca.fit_transform(variety_onehot)

print(new_var.shape)
print(pca.explained_variance_ratio_)

new_prov = pca.fit_transform(province_onehot)
print(pca.explained_variance_ratio_)

vintage_data = pd.read_csv("winemag-data-130k-v2 vintage merge.csv")
vintage_data.head()

var_PCA = pd.DataFrame({'var_PCA0':new_var[:,0],'var_PCA1':new_var[:,1],'var_PCA2':new_var[:,2],'var_PCA3':new_var[:,3],'var_PCA4':new_var[:,4]})

prov_PCA = pd.DataFrame({'prov_PCA0':new_prov[:,0],'prov_PCA1':new_prov[:,1],'prov_PCA2':new_prov[:,2],'prov_PCA3':new_prov[:,3],'prov_PCA4':new_prov[:,4]})

vintage_data = pd.DataFrame({'vintage':vintage_data.loc[:,'vintage']})

normalized_vintage=(vintage_data-vintage_data.mean())/vintage_data.std()

clustering_data = pd.concat([var_PCA, prov_PCA, normalized_vintage], axis = 1)

clustering_data = clustering_data.dropna()
print(clustering_data.shape)
clustering_data.head()

def label_count(labels):

	lab_count = dict()

	for x in labels:
		if x in lab_count:
			lab_count[x] += 1
		else:
			lab_count[x] = 1

	print(lab_count)

	return

n = 5

# not enough memory to run

cluster = AgglomerativeClustering(n_clusters=n, affinity='euclidean', linkage='average').fit(clustering_data)

labels = cluster.labels_
print("\n\nClusters:")
label_count(labels)

