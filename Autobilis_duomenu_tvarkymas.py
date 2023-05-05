import pandas as pd

df = pd.read_excel("Autobilis skelbimai_GALUTINIS.xlsx")
df.info()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.replace('\xa0', '')
        df[col] = df[col].str.replace('km', '')
        df[col] = df[col].str.replace(' kW', '')
        df[col] = df[col].str.replace('€', '')
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

df_clean = df.copy()

klaidos = []
for col in ['Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas']:
    skaicius = df_clean[col].str.isnumeric()
    klaidos_col = df_clean[skaicius][col].tolist()
    klaidos += klaidos_col
    print(f"{len(klaidos_col)} netinkamos reikšmės stulpelyje {col}")

df_clean = df_clean[~df_clean.isin(klaidos)].dropna()
print(f"Po išmetimo, DataFrame yra dydžio {df_clean.shape}")

df_clean = df_clean.reset_index(drop=True)
df_clean.to_csv('df_clean.csv', index=False)