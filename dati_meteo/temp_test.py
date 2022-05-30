import pandas as pd
from scipy import stats

#getting data for 2020 and 2021 temperature

df = pd.read_excel('./dati_meteo.xlsx', parse_dates = [1])
indice = [x for x in range(len(df))]
df['Indice'] = indice
anni = []
mesi = []
giorni = []
tmed = []
date = list(df['Giorno'].astype(str))
for i in indice:
	data_provv = df[df['Indice'] == i]
	data = list(data_provv['Giorno'].astype(str))[0]
	anni.append(data.split('-')[0])
	mesi.append(data.split('-')[1])
	giorni.append(data.split('-')[2])
	mintemp = df[df['Indice'] == i]['Tmin'].astype(float).values[0]
	maxtemp = df[df['Indice'] == i]['Tmax'].astype(float).values[0]
	tmed.append((mintemp + maxtemp) / 2)
df['Tmed'] = tmed
print(df['Tmed'])
comuni = list(set(df['Comune']))
df['Year'] = anni
df['Months'] = mesi
df['Giorni'] = giorni
mask11 = (df['Months'] != '11')
mask12 = (df['Months'] != '12')
masky = (df['Year'] != '2019')
df_ok = df[mask11]
df_ok_ok = df_ok[mask12]
df = df_ok_ok[masky]

df_2020 = df[df['Year'] == '2020']
df_2021 = df[df['Year'] == '2021']


df_2020 = df_2020[~((df_2020['Months'] == '02') & (df_2020['Giorni'] == '29'))]
print(df_2020)
print(df_2021)
with open('./stats/general_stats.txt', 'w') as f:
	for comune in comuni:
		com_2020 = df_2020[df_2020['Comune'] == comune]
		com_2021 = df_2021[df_2021['Comune'] == comune]
		tmin2020 = com_2020['Tmin']
		tmax2020 = com_2020['Tmax']
		tmed2020 = com_2020['Tmed']
		tmin2021 = com_2021['Tmin']
		tmax2021 = com_2021['Tmax']
		tmed2021 = com_2021['Tmed']
		minstat = stats.ttest_rel(tmin2020, tmin2021)
		maxstat = stats.ttest_rel(tmax2020, tmax2021)
		medstat = stats.ttest_rel(tmed2020, tmed2021)
		minmed = (tmin2020.mean(), tmin2021.mean())
		maxmed = (tmax2020.mean(), tmax2021.mean())
		medmed = (tmed2020.mean(), tmed2021.mean())
		minstd = (tmin2020.std(), tmin2021.std())
		maxstd = (tmax2020.std(), tmax2021.std())
		medstd = (tmed2020.std(), tmed2021.std())
		f.write(f'################## {comune}\nTmin2020: {minmed[0]} - {minstd[0]}\nTmax2020: {maxmed[0]} - {maxstd[0]}\nTmed2020: {medmed[0]} - {medstd[0]}\n')
		f.write(f'Tmin2021: {minmed[1]} - {minstd[1]}\nTmax2021: {maxmed[1]} - {maxstd[1]}\nTmed2021: {medmed[1]} - {medstd[1]}\n')
		f.write(f'Min temp stat: Tstat = {minstat[0]} - Pval = {minstat[1]}\n')
		f.write(f'Max temp stat: Tstat = {maxstat[0]} - Pval = {maxstat[1]}\n')
		f.write(f'med temp stat: Tstat = {medstat[0]} - Pval = {medstat[1]}\n')

months = '01,02,03,04,05,06,07,08,09,10'.split(',')
comuni = list(set(df['Comune']))
for comune in comuni:
	print(f'############# {comune} ############')
	com2020 = df_2020[df_2020['Comune'] == comune]
	com2021 = df_2021[df_2021['Comune'] == comune]
	tab = []
	for mese in months:
		mese2020 = com2020[com2020['Months'] == mese]['Tmed']
		mese2021 = com2021[com2021['Months'] == mese]['Tmed']
		med2020 = mese2020.mean()
		med2021 = mese2021.mean()
		std2020 = mese2020.std()
		std2021 = mese2021.std()
		stat = stats.ttest_rel(mese2020, mese2021)
		row = [med2020, std2020, med2021, std2021, stat[0], stat[1]]
		tab.append(row)
	print(tab)
	dfstats = pd.DataFrame(tab)
	dfstats.index = 'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct'.split(',')
	dfstats.columns = 'med2020,std2020,med2021,std2021,Tstat,Pval'.split(',')
	dfstats.to_csv(f'./stats/months/{comune}_temp.tsv', sep = '\t')