import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# nuskaitome modeliui kurti naudotus duomenis
df = pd.read_excel('Autobilis_skelbimai.xlsx')

# išvalome duomenis
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


# Suskirstome stulpelius pagal jų tipą
numeric_features = ['Metai', 'Variklio_galia', 'Rida']
categorical_features = ['Marke', 'Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas']

# Transformuojame numerinius stulpelius standartizavimo objektu
numeric_transformer = StandardScaler()

# Transformuojame kategorinius stulpelius kodavimo objektu
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Susiejame transformavimo objektus naudojant ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Susiejame preprocessor ir modelio objektus naudojant Pipeline
rf_regressor = Pipeline(steps=[('preprocessor', preprocessor),
                              ('regressor', RandomForestRegressor())])

# Pasiruošiame mokymo ir testavimo duomenis
X = df.drop('Kaina', axis=1)
y = df['Kaina']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apmokiname modelį
rf_regressor.fit(X_train, y_train)

# Skaičiuojame modelio tikslumą su testavimo duomenimis
accuracy = rf_regressor.score(X_test, y_test)
print("Modelio tikslumas: %.2f" % accuracy)

# Apskaičiuojame mean_squared_error reikšmę su testavimo duomenimis
y_pred = rf_regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("MSE reikšmė su testavimo duomenimis: %.2f" % mse)


# Įkeliam naujus duomenis
df_nauji = pd.read_csv('duomenys_spejimui.csv', delimiter=';', encoding='cp1257')

# Išvalom duomenis
df_nauji = clean_data(df_nauji)

# Paduodame duomenis modeliui
prognozes = rf_regressor.predict(df_nauji)

# sukurti naują stulpelį naudojant gautas prognozes
df_su_prognozes = df_nauji.assign(predictions=prognozes)

# išsaugoti atnaujintą duomenų rinkinį
df_su_prognozes.to_csv("duomenys_su_prognozemis.csv", index=False)

# Spausdinam prognozes
# print(prognozes)