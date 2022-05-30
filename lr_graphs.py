import pandas as pd
import numpy as np
from scipy.stats import linregress as lr
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_context('paper')
#reading general data
df = pd.read_csv('./dati_lr.csv', header = 0, index_col = 0)
print(df)

#Plotting LR for P. avium
#	shown an R2 > 0.6 for all variables against total precipitation
data = df[df['Species'] == 'Prunus avium']

sns.lmplot(data = data, x = 'Phenolics', y = 'Prec', ci = None)
plt.savefig('./plots/linear_regressions/pavium_phenolics_precipitation.png', dpi = 300)

sns.lmplot(data = data, x = 'Flavonoids', y = 'Prec', ci = None)
plt.savefig('./plots/linear_regressions/pavium_flavonoids_precipitation.png', dpi = 300)

sns.lmplot(data = data, x = 'FRAP', y = 'Prec', ci = None)
plt.savefig('./plots/linear_regressions/pavium_frap_precipitation.png', dpi = 300)

#Plotting LR for P. domestica
#	shown an R2 > 0.6 for Flav X Tmed / Flav x Tmax
data = df[df['Species'] == 'Prunus domestica']

sns.lmplot(data = data, x = 'Flavonoids', y = 'Tmed', ci = None)
plt.savefig('./plots/linear_regressions/pdom_flavonoids_tmed.png', dpi = 300)

sns.lmplot(data = data, x = 'Flavonoids', y = 'Tmax', ci = None)
plt.savefig('./plots/linear_regressions/pdom_flavonoids_tmax.png', dpi = 300)