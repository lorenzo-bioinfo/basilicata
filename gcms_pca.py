import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px

#getting gcms data
gcms_df = pd.read_csv('./dati_gcms/gcms_data_nan_locations.tsv', sep = '\t', header = 0, index_col = 0)

#saving year, species and location columns for further use
years = list(gcms_df['Year'])
species = list(gcms_df['Spec'])
locs = list(gcms_df['Location'])

#removing non-molecule columns
df_clean = gcms_df.drop(['Year', 'Spec', 'Location'], axis = 1).fillna(0)
print(df_clean)

#standardizing data
# z = (x - u)/S
#with:
#	z = scaled value
#	x = original value
#	u = column/feature mean
#	S = standard deviation of column/feature
df_std = pd.DataFrame(StandardScaler().fit_transform(df_clean))
df_std.columns = df_clean.columns
df_std.index = df_clean.index

#performing pca with 2 components
pca = PCA(n_components = 2)
principal_components = pca.fit_transform(df_std)
pca_df = pd.DataFrame(data = principal_components, columns = ['PC1', 'PC2'])
pca_df['Species'] = species
pca_df['Location'] = locs
pca_df['Year'] = years
pca_df.index = df_clean.index
print(pca_df)
with open('./plots/pca_scatterplots_gcms/explained_variance_2PC.txt', 'w') as varfile:
	varfile.write(f'Explained variance = {pca.explained_variance_ratio_}, Tot = {sum(pca.explained_variance_ratio_)}\n')
print(pca.singular_values_)

#plotting 2d scatterplots
sns.scatterplot(data = pca_df, x = 'PC1', y = 'PC2', hue = 'Species')
plt.savefig('./plots/pca_scatterplots_gcms/2d_species.png', dpi = 300)
plt.clf()
sns.scatterplot(data = pca_df, x = 'PC1', y = 'PC2', hue = 'Location')
plt.savefig('./plots/pca_scatterplots_gcms/2d_locations.png', dpi = 300)
plt.clf()
sns.scatterplot(data = pca_df, x = 'PC1', y = 'PC2', hue = 'Year')
plt.savefig('./plots/pca_scatterplots_gcms/2d_year.png', dpi = 300)
plt.clf()

#performing pca with 3 components
pca = PCA(n_components = 3)
principal_components = pca.fit_transform(df_std)
pca_df = pd.DataFrame(data = principal_components, columns = ['PC1', 'PC2', 'PC3'])
pca_df['Species'] = species
pca_df['Location'] = locs
pca_df['Year'] = years
pca_df.index = df_clean.index
print(pca_df)
with open('./plots/pca_scatterplots_gcms/explained_variance_3PC.txt', 'w') as varfile:
	varfile.write(f'Explained variance = {pca.explained_variance_ratio_}, Tot = {sum(pca.explained_variance_ratio_)}\n')
print(pca.singular_values_)

#plotting 3d scatterplots
fig = px.scatter_3d(pca_df, x = 'PC1', y = 'PC2', z = 'PC3', color = 'Species', title = 'GC-MS PCA 2021')
fig.show()
del fig
fig = px.scatter_3d(pca_df, x = 'PC1', y = 'PC2', z = 'PC3', color = 'Location', title = 'GC-MS PCA 2021')
fig.show()
del fig
fig = px.scatter_3d(pca_df, x = 'PC1', y = 'PC2', z = 'PC3', color = 'Year', title = 'GC-MS PCA 2021')
fig.show()
del fig