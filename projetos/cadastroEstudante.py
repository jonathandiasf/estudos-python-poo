import json

class Estudante:

  def __init__(self, nome, idade, matricula):
    self.nome = nome
    self.idade = idade
    self.matricula = matricula

  def cadastrar_estudante(self):
    self.nome = input('Digite o nome do estudante: ')
    self.idade = input('Digite a idade do estudante: ')
    self.matricula = input('Digite a matricula do estudante: ')

  def alterar_estudante(self):
    self.nome = input ('Digite o novo nome do estudante: ')
    self.idade = input ('Digite a nova idade do estudante: ')
    self.matricula = input ('Digite a nova matricula do estudante: ')

  def remover_estudante(self):
    self.nome = ''
    self.idade = ''
    self.matricula = ''

  def listar_estudante(self):
    print(f'Nome: {self.nome}')
    print(f'Idade: {self.idade}')
    print(f'Matricula: {self.matricula}')

  def to_dict(self):
    return {
        "nome": self.nome,
        "idade": self.idade,
        "matricula": self.matricula
    }

class SistemaEstudantes:
  def __init__(self, filename='estudantes.json'):
    self.filename = filename
    self.estudantes = []
    self.carregar_dados()

  def adicionar_estudante(self, estudante):
    self.estudantes.append(estudante)

  # This method was empty and is no longer needed as alteration is handled by Estudante class
  # def alterar_estudante(self):
  #   pass

  def listar_todos_estudantes(self):
    if not self.estudantes:
      print("Nenhum estudante cadastrado.")
      return
    print("\n--- Lista de Estudantes ---")
    for i, estudante in enumerate(self.estudantes):
      print(f"Estudante {i+1}:")
      estudante.listar_estudante()
      print("---------------------------")

  def salvar_dados(self):
    dados_para_salvar = [estudante.to_dict() for estudante in self.estudantes]
    with open(self.filename, 'w') as arquivo:
      json.dump(dados_para_salvar, arquivo, indent=2)
    print(f"Dados salvos em '{self.filename}'.")

  def carregar_dados(self):
    try:
      with open(self.filename, 'r') as arquivo:
        dados = json.load(arquivo)
        self.estudantes = [Estudante(d['nome'], d['idade'], d['matricula']) for d in dados]
      print(f"Dados carregados de '{self.filename}'.")
    except FileNotFoundError:
      print(f"Arquivo '{self.filename}' não encontrado. Iniciando com lista vazia de estudantes.")
    except json.JSONDecodeError:
      print(f"Erro ao decodificar JSON do arquivo '{self.filename}'. Iniciando com lista vazia de estudantes.")

# --- Demonstração de uso com menu ---
sistema = SistemaEstudantes()

while True:
    print("\n--- Menu de Opções ---")
    print("1. Cadastrar novo estudante")
    print("2. Editar estudante existente")
    print("3. Remover estudante")
    print("4. Listar todos os estudantes")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\n--- Cadastrar Novo Estudante ---")
        novo_estudante = Estudante('', '', '')
        novo_estudante.cadastrar_estudante()
        sistema.adicionar_estudante(novo_estudante)
        sistema.salvar_dados()
        print("Estudante cadastrado e salvo com sucesso.")
    elif opcao == '2':
        print("\n--- Editar Estudante ---")
        sistema.listar_todos_estudantes()
        if sistema.estudantes:
            try:
                indice_para_editar = int(input("Digite o número do estudante que deseja editar: "))
                if 1 <= indice_para_editar <= len(sistema.estudantes):
                    estudante_para_editar = sistema.estudantes[indice_para_editar - 1]
                    estudante_para_editar.alterar_estudante()
                    sistema.salvar_dados()
                    print("Dados do estudante alterados e salvos com sucesso.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    elif opcao == '3':
        print("\n--- Remover Estudante ---")
        sistema.listar_todos_estudantes()
        if sistema.estudantes:
            try:
                indice_para_remover = int(input("Digite o número do estudante que deseja remover: "))
                if 1 <= indice_para_remover <= len(sistema.estudantes):
                    estudante_para_remover = sistema.estudantes[indice_para_remover - 1]
                    estudante_para_remover.remover_estudante()
                    sistema.salvar_dados()
                    print("Dados do estudante removidos e salvos com sucesso.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    elif opcao == '4':
        sistema.listar_todos_estudantes()
    elif opcao == '5':
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")