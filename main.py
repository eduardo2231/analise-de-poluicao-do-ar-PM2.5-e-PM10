import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.sandbox.distributions.sppatch import expect

pd.set_option('display.max_rows', 100) # Max de linhas que vai aparcer
contents = pd.read_csv('verso.csv')
print(contents.loc[:99, ['Month', 'PM2.5','PM10']])

    # sum1 = contents['PM2.5'].sum()  # soma uma coluna
    # sum2 = contents['PM10'].sum()

monthly_sums = contents.groupby('Month')[['PM2.5', 'PM10']].sum() # aqui usa o Groupby

monthly_sums_4meses = monthly_sums.loc[[1, 2, 3, 4]] # filtrando pra apenas 4 meses

    # fig, axs = plt.subplots(1, 2, figsize=(12, 6)) #axs é um array cria

# Estatísticas para PM2.5
media_pm25 = np.mean(monthly_sums_4meses['PM2.5'])
mediana_pm25 = np.median(monthly_sums_4meses['PM2.5'])
q1_pm25 = np.percentile(monthly_sums_4meses['PM2.5'], 25)
q3_pm25 = np.percentile(monthly_sums_4meses['PM2.5'], 75)
iqr_pm25 = q3_pm25 - q1_pm25
desvio_pm25 = np.std(monthly_sums_4meses['PM2.5'], ddof=1)

# Estatísticas para PM10
media_pm10 = np.mean(monthly_sums_4meses['PM10'])
mediana_pm10 = np.median(monthly_sums_4meses['PM10'])
q1_pm10 = np.percentile(monthly_sums_4meses['PM10'], 25)
q3_pm10 = np.percentile(monthly_sums_4meses['PM10'], 75)
iqr_pm10 = q3_pm10 - q1_pm10
desvio_pm10 = np.std(monthly_sums_4meses['PM10'], ddof=1)

rotulos = ['Janeiro', 'Fevereiro', 'Março', 'Abril']

fig = plt.figure(figsize=(12, 10))
fig.suptitle("Poluição nos meses de Janeiro até Abril")

texto = (
    f"PM2.5 - Média: {media_pm25:.2f}, Mediana: {mediana_pm25:.2f}, IQR: {iqr_pm25:.2f}, "
    f"Q1: {q1_pm25:.2f}, Q3: {q3_pm25:.2f}, Desvio padrão: {desvio_pm25:.2f}\n"
    f"PM10 - Média: {media_pm10:.2f}, Mediana: {mediana_pm10:.2f}, IQR: {iqr_pm10:.2f}, "
    f"Q1: {q1_pm10:.2f}, Q3: {q3_pm10:.2f}, Desvio padrão: {desvio_pm10:.2f}"
)

fig.text(0.5, 0.02, texto, ha='center', fontsize=12)

gs = fig.add_gridspec(2, 2)

ax1 = fig.add_subplot(gs[0, 0])
ax1.pie(monthly_sums_4meses['PM10'].values, labels=rotulos, autopct="%1.1f%%")
ax1.set_title('PM10')

ax2 = fig.add_subplot(gs[0, 1])
ax2.pie(monthly_sums_4meses['PM2.5'].values, labels=rotulos, autopct="%1.1f%%")# autopct server pra pra mostrar um numero com uma casa decimal
ax2.set_title('PM2.5')

ax3 = fig.add_subplot(gs[1, 0])
ax3.bar(rotulos, monthly_sums_4meses['PM2.5'].values, color='Black')
ax3.set_ylabel('Soma PM2.5')
ax3.set_xlabel('Meses')
ax3.set_title('PM2.5 nos meses')

ax4 = fig.add_subplot(gs[1, 1])
ax4.bar(rotulos, monthly_sums_4meses['PM10'].values, color='Black')
ax4.set_ylabel('Soma PM10')
ax4.set_xlabel('Meses')
ax4.set_title('PM10 nos meses')

plt.show()

