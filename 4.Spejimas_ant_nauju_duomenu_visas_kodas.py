import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split


df = pd.read_csv('train_duomenys.csv')

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

    for col in ['Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas']:
        skaicius = df[col].str.isnumeric()
        klaidos_col = df[skaicius][col].tolist()
        df = df[~df[col].isin(klaidos_col)]
        df[col] = df[col].astype(str).str.lower().str.strip()

    df.reset_index(drop=True, inplace=True)
    return df

df = clean_data(df)


numeric_features = ['Metai', 'Variklio_galia', 'Rida']
categorical_features = ['Marke', 'Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas']

numeric_transformer = StandardScaler()

categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

rf_regressor = Pipeline(steps=[('preprocessor', preprocessor),
                              ('regressor', RandomForestRegressor())])

X = df.drop('Kaina', axis=1)
y = df['Kaina']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_regressor.fit(X_train, y_train)

accuracy = rf_regressor.score(X_test, y_test)
print("Modelio tikslumas: %.2f" % accuracy)


df_nauji = pd.read_csv('test_duomenys.csv')

df_nauji = clean_data(df_nauji)
df_nauji = df_nauji.drop('Kaina', axis=1)

prognozes = rf_regressor.predict(df_nauji)

df_su_prognozes = df_nauji.assign(predictions=prognozes)

df_su_prognozes.to_csv("prognozes.csv", index=False)
