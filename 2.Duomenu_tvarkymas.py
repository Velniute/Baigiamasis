import pandas as pd

df = pd.read_csv("train_duomenys.csv")
df.info()

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