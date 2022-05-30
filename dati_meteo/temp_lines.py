import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_theme(context = 'paper')
plt.figure(figsize = (13, 8))

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
		df2020_m = df2020[mask0]
		df2021_m = df2021[mask1]
		tmin_2020 = df2020_m['Tmin'].mean()
		tmax_2020 = df2020_m['Tmax'].mean()
		tmed2020 = (tmin_2020 + tmax_2020) / 2
		tmin_2021 = df2021_m['Tmin'].mean()
		tmax_2021 = df2021_m['Tmax'].mean()
		tmed2021 = (tmin_2021 + tmax_2021) / 2
		dict2020[str(i-1)] = (mesi[i - 1], 2020, tmin_2020, tmax_2020, tmed2020)
		dict2021[str(i-1)] = (mesi[i - 1], 2021, tmin_2021, tmax_2021, tmed2021)
	df_data2020 = pd.DataFrame.from_dict(dict2020, orient = 'index', columns = 'Month,Year,Tmin,Tmax,Tmed'.split(','))
	df_data2021 = pd.DataFrame.from_dict(dict2021, orient = 'index', columns = 'Month,Year,Tmin,Tmax,Tmed'.split(',')) 
	df_data = df_data2020.append(df_data2021, ignore_index = True)
	palette = sns.color_palette("magma_r", 2)
	sns.lineplot(data = df_data, x = 'Month', y = 'Tmin', markers = True, dashes = False, style = "Year", hue = 'Year', palette = palette).set_title('Mean minimum T °C')
	plt.savefig(f'./plots/temp/{comune}_lineplot_tmin.png', dpi = 300)
	plt.clf()
	sns.lineplot(data = df_data, x = 'Month', y = 'Tmax', markers = True, dashes = False, style = "Year", hue = 'Year', palette = palette).set_title('Mean maximum T °C')
	plt.savefig(f'./plots/temp/{comune}_lineplot_tmax.png', dpi = 300)
	plt.clf()
	sns.lineplot(data = df_data, x = 'Month', y = 'Tmed', markers = True, dashes = False, style = "Year", hue = 'Year', palette = palette).set_title('Mean T °C')
	plt.savefig(f'./plots/temp/{comune}_lineplot_tmed.png', dpi = 300)
	plt.clf()