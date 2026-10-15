from pandas import pandas
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt

# Exemplo de dados com valores de pacientes hospitalares, incluindo valores ausentes (None)

dados = {
    'idade': [25, 30, 35, None, 40],
    'peso': [70, 80, None, 90, 100],
    'altura': [1.75, 1.80, 1.65, None, 1.70],
    'presao_arterial': [120, 130, 140, 150, None],
    'colesterol': [200, 220, 240, None, 260],
    'tireoide': [1.5, 2.0, None, 2.5, 3.0],
    'diabetes': [0, 1, 0, 1, None],
    'fumante': [0, 1, None, 0, 1],
    'batimento_cardiaco': [70, 75, 80, 85, None]
}

# Criando um DataFrame a partir dos dados

df = pandas.DataFrame(dados)

# mostrando o DataFrame original
print("DataFrame original:")
print(df)

# Imputação de valores ausentes usando a média

imputer = SimpleImputer(strategy='mean')
df_imputed = pandas.DataFrame(imputer.fit_transform(df), columns=df.columns)

# mostrando o DataFrame após a imputação
print("\nDataFrame após a imputação de valores ausentes:")
print(df_imputed)

# Normalização dos dados

scaler_minmax = StandardScaler()
df_normalized = pandas.DataFrame(scaler_minmax.fit_transform(df_imputed), columns=df.columns)

# Mostrando o DataFrame após a normalização
print("\nDataFrame após a normalização:")
print(df_normalized)