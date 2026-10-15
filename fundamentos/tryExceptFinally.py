
print("Demonstração de tratamento de erros com try, except, else e finally")
try:
    numerador = 10
    denominador = int(input("Digite um número para dividir 10: "))
    resultado = numerador / denominador
    print(f"Resultado da divisão: {resultado}")
except ZeroDivisionError:
    # Captura erro de divisão por zero
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    # Captura erro quando a conversão para int falha
    print("Erro: Por favor, digite um número inteiro válido.")
except Exception as e:
    # Captura qualquer outro erro inesperado
    print(f"Ocorreu um erro inesperado: {e}")
else:
    # Executado apenas se nenhum erro acontecer no bloco try
    print("Divisão realizada com sucesso!")
finally:
    # Sempre executado, ocorrendo erro ou não
    print("Fim da execução do tratamento de erro.")
    print("--------------------------------------------")

print("Array com diferentes tipos de dados para demonstrar o tratamento de erros")
dados = [10, 5, 0, "texto", 2]

for valor in dados:
    print(f"\nProcessando o valor: {valor}")
    try:
        # Tenta realizar uma operação (dividir 100 pelo valor do array)
        resultado = 100 / valor
        print(f"Sucesso! 100 dividido por {valor} é igual a {resultado:.2f}")
    except ZeroDivisionError:
        # Trata o erro caso o elemento do array seja zero
        print("Erro: Divisão por zero detectada!")
    except TypeError:
        # Trata o erro caso o tipo de dado não seja numérico
        print(f"Erro: Tipo de dado inválido '{type(valor).__name__}' para divisão!")
    except Exception as e:
        # Trata qualquer outro erro genérico
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        # Bloco que sempre será executado ao final de cada iteração
        print(f"Finalizada a tentativa para o valor: {valor}")
        print("--------------------------------------------")
print("\n--- Demonstração de tratamento de erros com interface interativa ---")
import ipywidgets as widgets
from IPython.display import display, clear_output

# Criando os componentes da interface
num1_input = widgets.Text(description="Numerador:", value="10")
num2_input = widgets.Text(description="Denominador:", value="2")
calcular_btn = widgets.Button(description="Calcular", button_style="primary")
out = widgets.Output()

def executar_divisao(b):
    with out:
        clear_output() # Limpa o resultado anterior
        print("--- Iniciando Processamento ---")

        try:
            # Tenta converter as entradas para float e realizar a divisão
            n1 = float(num1_input.value)
            n2 = float(num2_input.value)
            resultado = n1 / n2
            print(f"Sucesso! O resultado de {n1} / {n2} é: {resultado:.2f}")

        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero!")

        except ValueError:
            print("Erro: Por favor, insira valores numéricos válidos!")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

        finally:
            # Este bloco sempre será executado ao final da operação
            print("--- Processamento Concluído (Bloco Finally) ---")

# Associa a função ao clique do botão
calcular_btn.on_click(executar_divisao)

# Exibe a interface
display(num1_input, num2_input, calcular_btn, out)