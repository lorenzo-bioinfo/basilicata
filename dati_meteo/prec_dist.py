import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_theme(context = 'paper')
plt.figure(figsize = (13, 8))
palette = sns.color_palette("mako_r", 2)


df = pd.read_excel('./dati_meteo.xlsx', parse_dates = [1])
anni = []
mesi = []
date = list(df['Giorno'].astype(str))
for data in date:
	anni.append(data.split('-')[0])
	mesi.append(data.split('-')[1])
comuni = list(set(df['Comune']))
df['Year'] = anni
df['Months'] = mesi
mask11 = (df['Months'] != '11')
mask12 = (df['Months'] != '12')
masky = (df['Year'] != '2019')
df_ok = df[mask11]
df_ok_ok = df_ok[mask12]
df = df_ok_ok[masky]
print(list(set(df['Months'])))
print(df)
for comune in comuni:
	df_com = df[df['Comune'] == comune]
	sns.displot(data = df_com, kind = 'kde', x = 'Prec', hue = 'Year', palette = palette)
	plt.savefig(f'./plots/prec/distplot/{comune}_precdist.png', dpi = 300)
	plt.clf()
for comune in comuni:
	df_com = df[df['Comune'] == comune]
	sns.displot(data = df_com, kind = 'hist', x = 'Prec', hue = 'Year', palette = palette)
	plt.savefig(f'./plots/prec/histplot/{comune}_prechist.png', dpi = 300)
	plt.clf()

for comune in comuni:
	df_com = df[df['Comune'] == comune]
	prec2020 = sum(list(df_com[df_com['Year'] == '2020']['Prec']))
	prec2021 = sum(list(df_com[df_com['Year'] == '2021']['Prec']))
	print(f'#####################{comune}\n2020tot = {prec2020}\n2021tot = {prec2021}\n')