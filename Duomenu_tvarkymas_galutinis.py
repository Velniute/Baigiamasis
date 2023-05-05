import pandas as pd


df = pd.read_excel("Autobilis skelbimai_GALUTINIS.xlsx")
df.info()


for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.replace('\xa0', '')
        df[col] = df[col].str.replace('km', '')
        df[col] = df[col].str.replace(' kW', '')
        df[col] = df[col].str.replace('€', '') s
        df[col] = df[col].str.replace('2+2', '')
        df[col] = df[col].str.replace(' ', '')
        df[col] = df[col].str.strip()


df['Metai'] = df['Metai'].str.replace('-\s\d+', '', regex=True).str.slice(stop=4)


for col in ['Rida', 'Variklio_galia']:
    df[col] = df[col].apply(lambda x: int(x) if str(x).isdigit() else 0)


df['Metai'] = pd.to_datetime(df['Metai'].str[:4], format='%Y')


df['Kaina'] = df['Kaina'].astype(int)


df = df.rename(columns={'Variklio_galia': 'Variklio_galia_kW', 'Rida': 'Rida_km', 'Kaina': 'Kaina_Eur.'})

df.info()


klaidos = []
isviso_klaidos = 0

for col in ['Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas']:
    for val in df[col]:
        if str(val).isnumeric():
            klaidos.append(val)
            isviso_klaidos += 1

print("Is viso eiluciu su klaidingomis reiksmemis:", isviso_klaidos)


klaidos_indeksai = df.index[df['Kebulo_tipas'].isin(klaidos) | df['Kuro_tipas'].isin(klaidos) |
                            df['Pavaru_dezes_tipas'].isin(klaidos)]


isvalytas_df = df.drop(klaidos_indeksai)
isvalytas_df