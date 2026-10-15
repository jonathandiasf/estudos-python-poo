from sklearn.model_selection import train_test_split
import pandas as pd

# Dados fictícios

dados = {
     'Idade' : ['20', '30'],
     'Salário' : ['2000', '3000'],
     'Comprador' : ['Sim', 'Não']
}

# Criando dataframe com os dados

df = pd.DataFrame(dados)

# Separar as features e o alvo (x, y)

x = df.drop('Comprador', axis=1) # Corrected column name to 'Comprador'
y = df['Comprador'] # Corrected to use bracket notation for column selection

# dividir os dados em conjuntos de treinamento e teste (80% treinamento e 20% teste)

X_treino, X_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=42)

# mostrar as dimensões de treinamento e teste 00
print(f"número de exemplo de treinamento em treino: {len(X_treino)}") # Corrected print statement
print(f"número de exemplo de treinamento em teste: {len(X_teste)}")   # Corrected print statement