import pandas as pd

df = pd.read_excel("Autobilis_skelbimai.xlsx")
df.info()

# 1 VARIANTAS
# for col in df.columns:
#     if df[col].dtype == 'object':
#         df[col] = df[col].str.replace('\xa0', '')
#         df[col] = df[col].str.replace('km', '')
#         df[col] = df[col].str.replace(' kW', '')
#         df[col] = df[col].str.replace('€', '')
#         df[col] = df[col].str.replace('2+2', '')
#         df[col] = df[col].str.replace(' ', '')
#         df[col] = df[col].str.strip()
#
#
# df['Metai'] = df['Metai'].str.replace('-\s\d+', '', regex=True).str.slice(stop=4)
#
# for col in ['Rida', 'Variklio_galia']:
#     df[col] = df[col].apply(lambda x: int(x) if str(x).isdigit() else 0)
#
# df['Metai'] = pd.to_datetime(df['Metai'].str[:4], format='%Y')
#
# df['Kaina'] = df['Kaina'].astype(int)
#
# df = df.rename(columns={'Variklio_galia': 'Variklio_galia_kW', 'Rida': 'Rida_km', 'Kaina': 'Kaina_Eur.'})
#
# df.info()
#
# df_clean = df.copy()
#
# klaidos = []
# for col in ['Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas']:
#     skaicius = df_clean[col].str.isnumeric()
#     klaidos_col = df_clean[skaicius][col].tolist()
#     klaidos += klaidos_col
#     print(f"{len(klaidos_col)} netinkamos reikšmės stulpelyje {col}")
#
# df_clean = df_clean[~df_clean.isin(klaidos)].dropna()
# print(f"Po išmetimo, DataFrame yra dydžio {df_clean.shape}")
#
# df_clean = df_clean.reset_index(drop=True)
# df_clean.to_csv('df_clean.csv', index=False)


#2 VARIANTAS - FUNKCIJA
# pašaliname nereikalingas tarpines eilutes, sutvarkome stulpelius
def clean_data(df):
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
    df['Metai'] = df['Metai'].astype(int)

    for col in ['Rida', 'Variklio_galia']:
        df[col] = df[col].apply(lambda x: int(x) if str(x).isdigit() else 0)

    df['Kaina'] = df['Kaina'].astype(int)

    for col in ['Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas']:
        skaicius = df[col].str.isnumeric()
        klaidos_col = df[skaicius][col].tolist()
        df = df[~df[col].isin(klaidos_col)]
        df[col] = df[col].astype(str).str.lower().str.strip()

    df.reset_index(drop=True, inplace=True)
    return df

df = clean_data(df)
df.info()

df.to_csv('df_clean.csv', index=False)
