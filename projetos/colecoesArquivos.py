print("1. Criando um arquivo de exemplo com dados de alunos")

dados_alunos = """Ana,8.5,9.0,7.5
Bruno,6.0,5.5,6.5
Carlos,4.0,5.0,3.0
Diana,9.0,10.0,9.5
"""

with open('notas_alunos.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(dados_alunos.strip())

print("Arquivo 'notas_alunos.txt' criado com sucesso!")
print("-----------------------------------------------------------------")
print ("2. Lendo o arquivo e utilizando coleções para manipular os dados")

alunos_processados = []

with open('notas_alunos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        # Limpa espaços e divide a linha pela vírgula
        partes = linha.strip().split(',')
        nome = partes[0]
        # Conversão das notas para float usando list comprehension (uma coleção)
        notas = [float(nota) for nota in partes[1:]]

        # Calculando a média
        media = sum(notas) / len(notas)

        # Determinando a situação
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"

        # Armazenando os dados estruturados em um dicionário
        aluno_dict = {
            'nome': nome,
            'notas': notas,
            'media': round(media, 2),
            'situacao': situacao
        }
        alunos_processados.append(aluno_dict)

# Exibindo a coleção criada
import pprint
pprint.pprint(alunos_processados)
print("-----------------------------------------------------------------")
print("3. Gravando os resultados processados em um novo arquivo")

with open('resultado_final_alunos.txt', 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write("Nome, Nota 1, Nota 2, Nota 3, Média, Situação\n")
    for aluno in alunos_processados:
        linha = f"{aluno['nome']}, {', '.join(map(str, aluno['notas']))}, {aluno['media']}, {aluno['situacao']}\n"
        arquivo_saida.write(linha)

print("Resultados salvos com sucesso em 'resultado_final_alunos.txt'!")

# exibindo o conteúdo do arquivo gerado
print("\n--- Conteúdo do Arquivo de Saída ---")
with open("resultado_final_alunos.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())
print("\n--------------------- Fim do Programa ----------------------------")