import pandas as pd
import os
import numpy as np
from scipy.stats import linregress as lr
from matplotlib import pyplot as plt
import seaborn as sns

#reading general data
df = pd.read_csv('./dati_lr.csv', header = 0, index_col = 0)
print(df)

#getting list of species
species = list(set(df['Species']))
print(species)
#defining list of variables for regression
xes = ['FRAP', 'Phenolics', 'Flavonoids']
yes = ['Tmin', 'Tmed', 'Tmax', 'Prec', 'Elevation']

for spec in species:
	specdf = df[df['Species'] == spec]
	#print(specdf)
	results = []
	for xvar in xes:
		part_res = []
		for yvar in yes:
			x = list(specdf[xvar])
			y = list(specdf[yvar])
			part_res.append(lr(x = x, y = y)[2]**2)
		results.append(part_res)
	spec_results = pd.DataFrame(results)
	spec_results.index = xes
	spec_results.columns = yes
	spec_results.to_csv(f'./lr_text/{spec}_lr.tsv', sep = '\t')

