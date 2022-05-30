import pandas as pd
from scipy.cluster import hierarchy
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_theme(context = 'paper')

#getting gcms data
df = pd.read_csv('./dati_gcms/gcms_data_with_nan.tsv', sep = '\t', header = 0, index_col = 0)
species = list(set(df['Spec']))
#removing non-molecule columns

for spec in species:
	df_toclust = df[df['Spec'] == spec].dropna(axis = 1, how = 'all').fillna(0).drop(['Year', 'Spec'], axis = 1)
	print(df_toclust)
	fitter = fitter = MinMaxScaler().fit(df_toclust)
	df_norm = pd.DataFrame(fitter.transform(df_toclust))
	df_norm.index = df_toclust.index
	df_norm.columns = df_toclust.columns
	
	#clustering non-normalized data
	cluster_col = hierarchy.linkage(df_toclust.T, method="ward", metric="euclidean")
	cluster_row = hierarchy.linkage(df_toclust, method="ward", metric="euclidean")
	clusterfig = sns.clustermap(df_toclust, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (20, 10), cmap = 'magma')
	index_col = clusterfig.dendrogram_col.reordered_ind #molecule
	index_row = clusterfig.dendrogram_row.reordered_ind #sample
	plt.savefig(f'./plots/gcms_clustering/species/{spec}_gcms_clust_magma.png', dpi = 300)
	plt.clf()
	clusterfig = sns.clustermap(df_toclust, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (20, 10), cmap = 'viridis')
	plt.savefig(f'./plots/gcms_clustering/species/{spec}_gcms_clust_viridis.png', dpi = 300)
	plt.clf()
	clusterfig = sns.clustermap(df_toclust, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (20, 10), cmap = 'mako')
	plt.savefig(f'./plots/gcms_clustering/species/{spec}_gcms_clust_mako.png', dpi = 300)
	plt.clf()

	cluster_col = hierarchy.linkage(df_norm.T, method="ward", metric="euclidean")
	cluster_row = hierarchy.linkage(df_norm, method="ward", metric="euclidean")
	clusterfig = sns.clustermap(df_norm, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (20, 10), cmap = 'magma')
	index_col = clusterfig.dendrogram_col.reordered_ind #molecule
	index_row = clusterfig.dendrogram_row.reordered_ind #sample
	plt.savefig(f'./plots/gcms_clustering/species/{spec}_gcms_clust(norm)_magma.png', dpi = 300)
	plt.clf()
	clusterfig = sns.clustermap(df_norm, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (20, 10), cmap = 'viridis')
	plt.savefig(f'./plots/gcms_clustering/species/{spec}_gcms_clust(norm)_viridis.png', dpi = 300)
	plt.clf()
	clusterfig = sns.clustermap(df_norm, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (20, 10), cmap = 'mako')
	plt.savefig(f'./plots/gcms_clustering/species/{spec}_gcms_clust(norm)_mako.png', dpi = 300)
	plt.clf()