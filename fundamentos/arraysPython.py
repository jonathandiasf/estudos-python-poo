print("1. As listas são a estrutura padrão do Python para armazenar coleções de itens. Elas são extremamente dinâmicas e podem conter elementos de tipos diferentes.")
# Criando uma lista convencional (pode conter tipos mistos)
lista_mista = [1, "Python", 3.14, True]
print("Lista mista:", lista_mista)

# Acessando elementos
print("Segundo elemento:", lista_mista[1])
print("________________________________________________________________________________________________________")
print("2. O Módulo Nativo array. Se você precisa de um array onde todos os elementos obrigatoriamente possuem o mesmo tipo básico (ex: apenas inteiros ou apenas floats) para economizar memória, você pode usar o módulo nativo array.")
import array

# O caractere 'i' define que o array aceita apenas inteiros com sinal
meu_array = array.array('i', [1, 2, 3, 4, 5])
print("Array nativo:", meu_array)

# Adicionando um elemento
meu_array.append(6)
print("Array após append:", meu_array)
print("________________________________________________________________________________________________________")
print("3. O Módulo NumPy. Para aplicações científicas e de engenharia, o NumPy é a biblioteca padrão para trabalhar com arrays. Ele oferece arrays multidimensionais e uma vasta gama de operações matemáticas.")
import numpy as np

# Criando um array do NumPy
np_array = np.array([1.5, 2.7, 3.9])
print("NumPy Array:", np_array)

# Operações matemáticas vetorizadas (diretamente no array)
print("Multiplicado por 2:", np_array * 2)
print("________________________________________________________________________________________________________")
print("4. O Módulo Pandas. Embora o Pandas seja mais conhecido por suas estruturas DataFrame e Series, ele também é construído sobre o NumPy e oferece funcionalidades avançadas para manipulação de dados tabulares.")

import pandas as pd
pd_array = pd.Series([10, 20, 30, 40])
print("Pandas Series:", pd_array)
print("Soma dos elementos:", pd_array.sum())
print("________________________________________________________________________________________________________")
print("5. O Módulo array do SciPy. Para aplicações mais avançadas, o SciPy oferece arrays que podem ser usados para computação científica, incluindo suporte a álgebra linear, otimização e estatísticas.")

import scipy
from scipy import sparse
# Criando uma matriz esparsa (sparse matrix)
sparse_matrix = sparse.csr_matrix([[0, 0, 3], [4, 0, 0], [0, 5, 0]])
print("Matriz esparsa (SciPy):")
print(sparse_matrix)
print("________________________________________________________________________________________________________")

print("6. Arrays unidimensionais e multidimensionais. Arrays podem ser unidimensionais (vetores) ou multidimensionais (matrizes, tensores). A escolha depende da aplicação e da necessidade de representar dados em diferentes dimensões.")

import numpy as np
# Criando um array unidimensional 1D (vetor)
array_1d = np.array([1, 2, 3, 4, 5])
print("Array 1D:", array_1d)
print("Forma do array 1D:", array_1d.shape)
print("Dimensões do array 1D:", array_1d.ndim)
print("Formato (shape) do array 1D:", array_1d.shape)

# Criando um array bidimensional 2D (matriz)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:", array_2d)
print("Forma do array 2D:", array_2d.shape)
print("Dimensões do array 2D:", array_2d.ndim)
print("Formato (shape) do array 2D:", array_2d.shape)
# acessando elementos do array 2D
print("Elemento na posição (0, 1):", array_2d[0, 1])  # Acessando o elemento da primeira linha, segunda coluna
print("Elemento na posição (1, 2):", array_2d[1, 2])  # Acessando o elemento da segunda linha, terceira coluna
print("________________________________________________________________________________________________________")

print("7. Operações com arrays. Arrays suportam operações matemáticas vetorizadas, o que significa que você pode realizar operações em todos os elementos do array de forma eficiente e concisa.")
import numpy as np
from numpy import array

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("Array A:", array_a)
print("Array B:", array_b)
print("Soma dos arrays:", array_a + array_b)
print("Subtração dos arrays:", array_a - array_b)
print("Multiplicação dos arrays:", array_a * array_b)
print("Divisão dos arrays:", array_a / array_b)

while True:
    print("\nEscolha uma operação para realizar com os arrays:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '1':
        resultado = array_a + array_b
        print("Resultado da soma:", resultado)
    elif escolha == '2':
        resultado = array_a - array_b
        print("Resultado da subtração:", resultado)
    elif escolha == '3':
        resultado = array_a * array_b
        print("Resultado da multiplicação:", resultado)
    elif escolha == '4':
        resultado = array_a / array_b
        print("Resultado da divisão:", resultado)
    elif escolha == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
    break
print("________________________________________________________________________________________________________")

print("8. Comparação entre listas e arrays. Listas são mais flexíveis, mas arrays são mais eficientes para operações matemáticas e manipulação de grandes volumes de dados.")
import numpy as np
from numpy import array
array_lista = [1, 2, 3, 4, 5]  # Lista convencional
array_numpy = np.array([1, 2, 3, 4, 5])  # Array do NumPy
print("Lista convencional:", array_lista)
print("Array do NumPy:", array_numpy)
print("Soma da lista convencional:", sum(array_lista))  # Soma usando a função nativa sum
print("Soma do array do NumPy:", np.sum(array_numpy))  # Soma usando a função do NumPy
print("________________________________________________________________________________________________________")
