import pandas as pd
import os
import numpy as np
from scipy.stats import linregress as lr
from matplotlib import pyplot as plt
import seaborn as sns

#reading general data
df = pd.read_excel('./matrixplot_data.xlsx')
print(df)
#defining list of variables for regression
xes = ['FRAP', 'Phenolics', 'Flavonoids']
yes = xes.copy()

results = []
for xvar in xes:
	part_res = []
	for yvar in yes:
		x = list(df[xvar])
		y = list(df[yvar])
		part_res.append(lr(x = x, y = y)[2]**2)
	results.append(part_res)
spec_results = pd.DataFrame(results)
spec_results.index = xes
spec_results.columns = yes
spec_results.to_csv('./lr_text/matrixplot_lr.tsv', sep = '\t')

#doing the same for terpenoids
df = df[df['Kind'] == 'O.']
xes = ['Terpenoids']
results = []
for xvar in xes:
	part_res = []
	for yvar in yes:
		x = list(df[xvar])
		y = list(df[yvar])
		part_res.append(lr(x = x, y = y)[2]**2)
	results.append(part_res)
spec_results = pd.DataFrame(results)
spec_results.index = xes
spec_results.columns = yes
spec_results.to_csv('./lr_text/matrixplot_lr(terpenoids).tsv', sep = '\t')