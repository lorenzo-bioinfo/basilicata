import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import os

sns.set_theme(context = 'paper')
#plt.figure(figsize = (13, 8))

df = pd.read_excel('./matrixplot_data.xlsx')
print(df)
print(df.columns)
#hue plant part
sns.pairplot(df, hue = 'Kind', vars = ['Phenolics', 'Flavonoids', 'Terpenoids', 'FRAP'], kind = 'reg', diag_kind = 'kde')
plt.savefig('./plots/matrix_kind.png', dpi = 300)
plt.clf()