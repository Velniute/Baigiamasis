import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Nuskaitome duomenų failą
df = pd.read_csv('df_clean.csv')

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


#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime
# from sklearn.pipeline import Pipeline
# from sklearn.compose import ColumnTransformer
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
#
# # nuskaitome duomenis
# df = pd.read_csv('df_clean.csv')
#
# num_features = ['Metai', 'Variklio_galia', 'Rida']
# cat_features = ['Marke', 'Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas']
#
# num_scaler = StandardScaler()
# num_transformed = num_scaler.fit_transform(df[num_features])
#
# cat_encoder = OneHotEncoder(handle_unknown='ignore')  # unknown categories will be set to zeros in the corresponding columns
# cat_encoded = cat_encoder.fit_transform(df[cat_features]).toarray()
#
# features = np.concatenate((num_transformed, cat_encoded), axis=1)
# print(features.shape)
#
# # suskirstome duomenis į mokymo ir testavimo rinkinius
# X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['Kaina']), df['Kaina'], test_size=0.2,
#                                                     random_state=42)
#
# # sukuriame Random Forest regresorių
# rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
#
# # apmokome modelį
# rf.fit(X_train, y_train)
#
# # numatome kainų vertes testavimo rinkinyje
# y_pred = rf.predict(X_test)
#
# # vertiname modelio tikslumą naudojant MSE metriką
# mse = mean_squared_error(y_test, y_pred)

print(f"MSE: {mse}")








# sudarome pipeline
# numeric_transformer = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='median')),
#     ('scaler', StandardScaler())])
#
# categorical_transformer = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='most_frequent')),
#     ('encoder', OneHotEncoder(handle_unknown='ignore'))])

# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', ['Metai', 'Variklio_galia', 'Rida']),
#         ('cat', ['Marke', 'Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas'])])
#
# # sudarome pilną pipeline su modeliu
# pipeline = Pipeline(steps=[('preprocessor', preprocessor),
#                            ('regressor', RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_leaf=10,
#                                                                random_state=42))])


# # apmokome modelį ir numatome kainų vertes testavimo rinkinyje
# pipeline.fit(X_train, y_train)
# y_pred = pipeline.predict(X_test)
#
# # vertiname modelio tikslumą naudojant MSE ir R^2 metrikas
# mse = mean_squared_error(y_test, y_pred)
# r2 = pipeline.score(X_test, y_test)
#
# print(f"MSE: {mse}")
# print(f"R2: {r2}")
