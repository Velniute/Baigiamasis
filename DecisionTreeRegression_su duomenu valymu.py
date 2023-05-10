import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

# nuskaitome duomenis
df = pd.read_csv('df_clean.csv')
df.info()
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

# 1 VARIANTAS
# # suskirstomi duomenys į mokymo ir testavimo rinkinius
# num_features = ['Metai', 'Variklio_galia', 'Rida']
# cat_features = ['Marke', 'Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas']
#
# num_scaler = StandardScaler()
# num_transformed = num_scaler.fit_transform(df[num_features])
#
# cat_encoder = OneHotEncoder(handle_unknown='ignore')
# cat_encoded = cat_encoder.fit_transform(df[cat_features]).toarray()
#
# X_train, X_test, y_train, y_test = train_test_split(np.concatenate((num_transformed, cat_encoded), axis=1), df['Kaina'].values, test_size=0.2, random_state=42)
#
# # apmokome modelį su mokymo rinkiniu
# tree_reg = DecisionTreeRegressor(random_state=42)
# tree_reg.fit(X_train, y_train)
#
# # įvertiname modelio veikimą su testavimo rinkiniu
# y_pred = tree_reg.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# print('RMSE:', rmse)
#
# # apskaičiuojame vidutinį kryžminį patikrinimo RMSE
# scores = cross_val_score(tree_reg, np.concatenate((X_train, X_test), axis=0), np.concatenate((y_train, y_test), axis=0),
#                          scoring='neg_root_mean_squared_error',
#                          cv=5)
# print('CV RMSE:', np.mean(-scores))


# 2 VARIANTAS SU PIPELINE
# suskirstome duomenis į mokymo ir testavimo rinkinius
# X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['Kaina']), df['Kaina'], test_size=0.2,
#                                                     random_state=42)
#
# # sudarome pipeline
# numeric_transformer = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='median')),
#     ('scaler', StandardScaler())])
#
# categorical_transformer = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='most_frequent')),
#     ('encoder', OneHotEncoder(handle_unknown='ignore'))])
#
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', numeric_transformer, ['Metai', 'Variklio_galia', 'Rida']),
#         ('cat', categorical_transformer, ['Marke', 'Kebulo_tipas', 'Kuro_tipas', 'Pavaru_dezes_tipas'])])
#
# # sudarome pilną pipeline su modeliu
# pipeline = Pipeline(steps=[('preprocessor', preprocessor),
#                            ('regressor', DecisionTreeRegressor(max_depth=5, min_samples_leaf=10, random_state=42))])
#
# # apmokome modelį ir numatome kainų vertes testavimo rinkinyje
# pipeline.fit(X_train, y_train)
# y_pred = pipeline.predict(X_test)
#
# # vertiname modelio tikslumą naudojant MSE ir R^2 metrikas
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# r2 = pipeline.score(X_test, y_test)
#
# print(f"MSE: {mse}")
# print(f"RMSE: {rmse}")
# print(f"R2: {r2}")
