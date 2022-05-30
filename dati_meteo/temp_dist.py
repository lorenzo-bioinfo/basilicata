import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_theme(context = 'paper')
plt.figure(figsize = (13, 8))
palette = sns.color_palette("magma_r", 2)


df = pd.read_excel('./dati_meteo.xlsx', parse_dates = [1])
anni = []
mesi = []
tmed = []
date = list(df['Giorno'].astype(str))
for data in date:
	anni.append(data.split('-')[0])
	mesi.append(data.split('-')[1])
	mintemp = df[df['Giorno'] == data]['Tmin'].astype(float).values[0]
	maxtemp = df[df['Giorno'] == data]['Tmax'].astype(float).values[0]
	tmed.append((mintemp + maxtemp) / 2)
df['Tmed'] = tmed
print(df['Tmed'])
comuni = list(set(df['Comune']))
df['Year'] = anni
df['Months'] = mesi
mask11 = (df['Months'] != '11')
mask12 = (df['Months'] != '12')
masky = (df['Year'] != '2019')
print(mask11)
df_ok = df[mask11]
df_ok_ok = df_ok[mask12]
df = df_ok_ok[masky]
print(list(set(df['Months'])))
print(df)

for comune in comuni:
	df_com = df[df['Comune'] == comune]
	sns.displot(data = df_com, kind = 'kde', x = 'Tmin', hue = 'Year', palette = palette)
	plt.savefig(f'./plots/temp/distplot/{comune}_mindist.png', dpi = 300)
	plt.clf()
	sns.displot(data = df_com, kind = 'kde', x = 'Tmed', hue = 'Year', palette = palette)
	plt.savefig(f'./plots/temp/distplot/{comune}_meddist.png', dpi = 300)
	plt.clf()
	sns.displot(data = df_com, kind = 'kde', x = 'Tmax', hue = 'Year', palette = palette)
	plt.savefig(f'./plots/temp/distplot/{comune}_maxdist.png', dpi = 300)
	plt.clf()

for comune in comuni:
	df_com = df[df['Comune'] == comune]
	sns.displot(data = df_com, kind = 'hist', x = 'Tmin', hue = 'Year', palette = palette)
	plt.savefig(f'./plots/temp/histplot/{comune}_mindist.png', dpi = 300)
	plt.clf()
	sns.displot(data = df_com, kind = 'hist', x = 'Tmed', hue = 'Year', palette = palette)
	plt.savefig(f'./plots/temp/histplot/{comune}_meddist.png', dpi = 300)
	plt.clf()
	sns.displot(data = df_com, kind = 'hist', x = 'Tmax', hue = 'Year', palette = palette)
	plt.savefig(f'./plots/temp/histplot/{comune}_maxdist.png', dpi = 300)
	plt.clf()