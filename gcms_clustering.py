import pandas as pd
from scipy.cluster import hierarchy
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_theme(context = 'paper')

#getting gcms data
gcms_df = pd.read_csv('./dati_gcms/gcms_data.tsv', sep = '\t', header = 0, index_col = 0)

#removing non-molecule columns
df_toclust = gcms_df.drop(['Year', 'Spec'], axis = 1)
print(df_toclust)

#normalizing data
fitter = MinMaxScaler().fit(df_toclust)
df_norm = pd.DataFrame(fitter.transform(df_toclust))
df_norm.index = df_toclust.index
df_norm.columns = df_toclust.columns
print(df_norm)

#clustering non-normalized data

cluster_col = hierarchy.linkage(df_toclust.T, method="ward", metric="euclidean")
cluster_row = hierarchy.linkage(df_toclust, method="ward", metric="euclidean")
clusterfig = sns.clustermap(df_toclust, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (10, len(df_toclust)/4), cmap = 'magma')
index_col = clusterfig.dendrogram_col.reordered_ind #molecule
index_row = clusterfig.dendrogram_row.reordered_ind #sample
plt.savefig('./plots/gcms_clustering/gcms_clust_full_magma.png', dpi = 300)
plt.clf()
clusterfig = sns.clustermap(df_toclust, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (10, len(df_toclust)/4), cmap = 'viridis')
plt.savefig('./plots/gcms_clustering/gcms_clust_full_viridis.png', dpi = 300)
plt.clf()
clusterfig = sns.clustermap(df_toclust, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (10, len(df_toclust)/4), cmap = 'mako')
plt.savefig('./plots/gcms_clustering/gcms_clust_full_mako.png', dpi = 300)
plt.clf()

cluster_col = hierarchy.linkage(df_norm.T, method="ward", metric="euclidean")
cluster_row = hierarchy.linkage(df_norm, method="ward", metric="euclidean")
clusterfig = sns.clustermap(df_norm, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (10, len(df_norm)/4), cmap = 'magma')
index_col = clusterfig.dendrogram_col.reordered_ind #molecule
index_row = clusterfig.dendrogram_row.reordered_ind #sample
plt.savefig('./plots/gcms_clustering/gcms_clust_full(norm)_magma.png', dpi = 300)
plt.clf()
clusterfig = sns.clustermap(df_norm, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (10, len(df_norm)/4), cmap = 'viridis')
plt.savefig('./plots/gcms_clustering/gcms_clust_full(norm)_viridis.png', dpi = 300)
plt.clf()
clusterfig = sns.clustermap(df_norm, row_linkage = cluster_row, col_linkage = cluster_col, yticklabels = True, figsize = (10, len(df_norm)/4), cmap = 'mako')
plt.savefig('./plots/gcms_clustering/gcms_clust_full(norm)_mako.png', dpi = 300)
plt.clf()