import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Nuskaitome duomenų failą
df = pd.read_excel('Autobilis_skelbimai.xlsx')

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


