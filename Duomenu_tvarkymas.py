import pandas as pd


df = pd.read_excel("Autobilis skelbimai_GALUTINIS.xlsx")
df.info()


for col in df.columns:
    if df[col].dtype == 'object': #tikrinu, ar stulpelis yra tekstinis
        df[col] = df[col].str.replace('\xa0', '') #išvalau \xa0 simbolius
        df[col] = df[col].str.replace('km', '') #išvalau km simbolius
        df[col] = df[col].str.replace(' kW', '') #išvalau kW simbolius
        df[col] = df[col].str.replace('€', '') #išvalau euro simbolius
        df[col] = df[col].str.replace('2+2', '')  #išvalau 2+2 simbolius Marke stulpelyje
        df[col] = df[col].str.replace(' ', '')  #išvalau tarpus tarp skaitmenu Kainu stulpelyje
        df[col] = df[col].str.strip()  #stulpeliuose pašalinu tarpus priekyje ir gale


# pašalinu nereikalingus simbolius iš Metai stulpelio reikšmių ir išlaikau tik pirmus 4 simbolius
df['Metai'] = df['Metai'].str.replace('-\s\d+', '', regex=True).str.slice(stop=4)


# iteruoju per stulpelius ir keičiu reikšmes
for col in ['Rida', 'Variklio_galia']:
    df[col] = df[col].apply(lambda x: int(x) if str(x).isdigit() else 0)

#keiciu tipa, bet vis tiek gaunasi timestamp, neina padaryti 4 skaitmenu/metu
df['Metai'] = pd.to_datetime(df['Metai'].str[:4], format='%Y')

df['Kaina'] = df['Kaina'].astype(int)

# pakeiciu stulpeliu pavadinimas
df = df.rename(columns={'Variklio_galia': 'Variklio_galia_kW', 'Rida': 'Rida_km', 'Kaina': 'Kaina_Eur.'})

df.info()


