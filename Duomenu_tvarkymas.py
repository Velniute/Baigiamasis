import pandas as pd
import re
import numpy as np

df = pd.read_excel("Autobilis skelbimai_GALUTINIS.xlsx")

#panaikinu \n
df = df.replace('\n', '', regex=True) #nuskaitant faila isirase \n simboliai, istrinu juos

#Is object stulpeliu eilutese isvalau tarpus pries ir po
# df.info()
for column in df.columns:
    if df[column].dtype == object:
        df[column] = df[column].str.strip()

#sutvarkau Metai stulpeli, kad rezultate liktu tik metai int formatu
df['Tik_metai'] = df['Metai'].apply(lambda x: x.split('-')[0]) #susikuriu nauja stulpeli ir i ji irasau skaicius be -5
# ir pan.
df = df.drop('Metai', axis=1) #istrinu originalu stulpeli
df = df.rename(columns={'Tik_metai': 'Metai'}) #pakeiciu pavadinimas
df['Metai'] = df['Metai'].str.strip() #panaikinu tarpus pries ir po skaiciaus, nes meta klaida
df['Metai'] = pd.to_datetime(df['Metai'], format='%Y') #pakeiciu formata i datetime, bet gaunu datestamp
df['Metai'] = df['Metai'].dt.year #pasilieku 4 skaicius ir gaunu int tipa


#Sutvarkau Kaina stulpeli, kad reiksmes butu int tipo ir be valiutos zenklo
df['Kaina'] = df['Kaina'].apply(lambda x: int(re.sub('[^0-9]', '', x))) #istrinu valiutos zenkla,gaunu int tipa


#Sutvarkau Rida stulpeli, kad neliktu \xa0 simboliu skaiciaus viduryje ir, kad neliktu km
df['Rida'] = df['Rida'].str.replace('\xa0', '') #istrinu \xa0 simbolius, kurie isirase nuskaitant faila
df['Rida'] = df['Rida'].str.replace('km', '') #istrinu km

df['Rida_copy'] = df['Rida'].copy() #sukuriu stulpelio kopija reiksmiu patikrinimui
df['Rida'] = pd.to_numeric(df['Rida'], errors='coerce') #keiciu reiksmes i skaicius, bet jei reiksme yra string,
# tada gaunasi nan
df['Rida'] = df['Rida'].fillna(value=0) # pakeiciu NaN reiksmes i 0
df['Rida'] = df['Rida'].astype(int) # keiciu reiksmiu tipa i int

# for index, row in df.iterrows():
#     try:
#         df.loc[index, 'Rida'] = int(row['Rida'])
#     except ValueError:
#         df.loc[index, 'Rida'] = np.nan   #iteruoju per stulpelio eilutes ir jei reiksme yra ne int, tai irasoma nan,
#bet lieka object tipas


#Sutvarkau Variklio_galia stulpeli ir pagal ji istrinu eilutes, kuriose reiksmes scrapinant sukrito ne i teisingus
# stulpelius
df['Variklio_galia'] = df['Variklio_galia'].str.replace('kW', '') #pasalinu kW
df['Variklio_galia_copy'] = df['Variklio_galia'].copy() #susikuriu stulpelio kopija patikrinimui

df['Variklio_galia'] = pd.to_numeric(df['Variklio_galia'], errors='coerce') #keiciu reiksmes i skaicius, bet jei
# reiksme yra string, tada gaunasi nan
df['Variklio_galia'] = df['Variklio_galia'].fillna(value=0) # pakeiciu NaN reiksmes i 0
df['Variklio_galia'] = df['Variklio_galia'].astype(int) # keiciu reiksmiu tipa i int

df.dropna(subset=['Variklio_galia'], inplace=True) #istrinu visas nan eilutes


#Sutvarkau Marke stulpeli, pasalinu 2+2 simbolius, kurie atsirado scrapinant
df['Marke'] = df['Marke'].str.replace('2+2', '')


#Sutvarkau Kebulo_tipas stulpeli:
df['Kebulo_tipas'] = df['Kebulo_tipas'].str.replace('kW', '')


#Reikia isrinkti visas eilutes, kuriose reiksmes sukritusios i netinkamus stulpelius.Variklio_galia kai yra 0,
# atrodo tada yra klaidos

df[df['Variklio_galia'] == 0]

df.info()
print(df['Variklio_galia'].dtype)




# unique = df['Marke'].unique()
# unique1 = df['Kebulo_tipas'].unique()



# df['Marke'] = df['Marke'].str.strip()  # pašalina tarpo simbolius pradžioje ir pabaigoje
# df['Marke'] = df['Marke'].astype(str)  # paverčia reikšmes į eilutes tipo
# df['Marke'] = df['Marke'].apply(lambda x: x.replace('simbolis', ''))  # panaikina nereikalingus simbolius
# unique_values = df['Marke'].unique()