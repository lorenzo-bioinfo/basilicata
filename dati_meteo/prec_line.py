import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_theme(context = 'paper')
plt.figure(figsize = (13, 8))
palette = sns.color_palette("mako_r", 2)

df = pd.read_excel('./dati_meteo.xlsx', parse_dates = [1])
print(df)

comuni = list(set(df['Comune']))
mask = df['Giorno'].dt.year == 2020
for comune in comuni:
	df_provv = df[df['Comune'] == comune]
	df_provv_2020 = df_provv[mask]
	df_provv_2020.to_csv(f'{comune}2020.csv')

mask = df['Giorno'].dt.year == 2021
for comune in comuni:
	df_provv = df[df['Comune'] == comune]
	df_provv_2021 = df_provv[mask]
	df_provv_2021.to_csv(f'{comune}2021.csv')
mesi = 'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec'.split(',')
for comune in comuni:
	df2020 = pd.read_csv(f'{comune}2020.csv', header = 0, index_col = 0, parse_dates = [2])
	df2021 = pd.read_csv(f'{comune}2021.csv', header = 0, index_col = 0, parse_dates = [2])
	dict2020 = {}
	dict2021 = {}
	for i in range(1, 13):
		mask0 = df2020['Giorno'].dt.month == i
		mask1 = df2021['Giorno'].dt.month == i
		df2020_m = df2020[df2020.Tipo_Prec != 'neve'][mask0]
		df2021_m = df2021[df2021.Tipo_Prec != 'neve'][mask1]
		meanprec_2020 = df2020_m['Prec'].mean()
		meanprec_2021 = df2021_m['Prec'].mean()
		dict2020[str(i-1)] = (mesi[i - 1], 2020, meanprec_2020)
		dict2021[str(i-1)] = (mesi[i - 1], 2021, meanprec_2021)
	df_data2020 = pd.DataFrame.from_dict(dict2020, orient = 'index', columns = 'Month,Year,Mean Prec'.split(','))
	df_data2021 = pd.DataFrame.from_dict(dict2021, orient = 'index', columns = 'Month,Year,Mean Prec'.split(',')) 
	df_data = df_data2020.append(df_data2021, ignore_index = True)
	df_data = df_data2020.append(df_data2021, ignore_index = True)
	sns.lineplot(data = df_data, x = 'Month', y = 'Mean Prec', markers = True, dashes = False, style = "Year", hue = 'Year', palette = palette).set_title('Mean Precipitation (mm)')
	plt.ylabel('Rain (mm)')
	plt.savefig(f'./plots/prec/{comune}_lineplot_prec.png', dpi = 300)
	plt.clf()