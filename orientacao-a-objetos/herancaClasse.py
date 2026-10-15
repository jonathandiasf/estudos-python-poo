class Animal():
    def __init__(self, nome, raça, cor):
        self.nome = nome
        self.raça = raça
        self.cor = cor

    def fazer_som(self):
        raise NotImplementedError("Subclasses devem implementar este método")

    def info(self):
        return f"Eu sou um animal chamado {self.nome} da raça {self.raça} e cor {self.cor}."

class Cachorro(Animal):
    def __init__(self, nome, raça, cor):
        super().__init__(nome, raça, cor)

    def fazer_som(self):
        return "Latido!"

class Cavalo(Animal):
    def __init__(self, nome, raça, cor):
        super().__init__(nome, raça, cor)

    def fazer_som(self):
        return "Relincho!"

class Gato(Animal):
    def __init__(self, nome, raça, cor):
        super().__init__(nome, raça, cor)

    def fazer_som(self):
        return "Miado!"

# Criando instâncias de animais iniciais
cachorro1 = Cachorro("Buddy", "Labrador", "Dourado")
cavalo1 = Cavalo("Spirit", "Mustang", "Marrom")
gato1 = Gato("Melo", "Viralata", "Cinza")

# Criando uma lista de animais que será gerenciada
lista_de_animais = [cachorro1, cavalo1, gato1]

# Helper functions for menu actions
def encontrar_animal(nome_busca, lista):
    for animal in lista:
        if animal.nome.lower() == nome_busca.lower():
            return animal
    return None

def listar_animais(lista):
    if not lista:
        print("Nenhum animal na lista.")
        return
    print("\n--- Lista de Animais ---")
    for animal in lista:
        print(animal.info())
        print(f"Som: {animal.fazer_som()}")
        print("-" * 20)

# Main interactive loop
while True:
    print ("\n--- MENU DE GERENCIAMENTO DE ANIMAIS ---")
    print ("1. Pesquisar Animal")
    print ("2. Adicionar Novo Animal")
    print ("3. Editar Animal")
    print ("4. Remover Animal")
    print ("5. Listar Todos os Animais")
    print ("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1": # Pesquisar Animal
        nome_pesquisa = input("Digite o nome do animal para pesquisar: ")
        animal_encontrado = encontrar_animal(nome_pesquisa, lista_de_animais)
        if animal_encontrado:
            print("\nAnimal encontrado:")
            print(animal_encontrado.info())
            print(f"Som: {animal_encontrado.fazer_som()}")
        else:
            print(f"Animal '{nome_pesquisa}' não encontrado.")

    elif opcao == "2": # Adicionar Novo Animal
        print("\n--- Adicionar Novo Animal ---")
        tipo_animal = input("Tipo (Cachorro, Cavalo, Gato): ").capitalize()
        nome = input("Nome: ")
        raca = input("Raça: ")
        cor = input("Cor: ")

        novo_animal = None
        if tipo_animal == "Cachorro":
            novo_animal = Cachorro(nome, raca, cor)
        elif tipo_animal == "Cavalo":
            novo_animal = Cavalo(nome, raca, cor)
        elif tipo_animal == "Gato":
            novo_animal = Gato(nome, raca, cor)
        else:
            print("Tipo de animal inválido.")

        if novo_animal:
            lista_de_animais.append(novo_animal)
            print(f"'{novo_animal.nome}' adicionado à lista.")

    elif opcao == "3": # Editar Animal
        nome_edicao = input("Digite o nome do animal para editar: ")
        animal_para_editar = encontrar_animal(nome_edicao, lista_de_animais)
        if animal_para_editar:
            print(f"\nEditando '{animal_para_editar.nome}' (Raça: {animal_para_editar.raça}, Cor: {animal_para_editar.cor})")
            nova_raca = input(f"Nova raça (deixe em branco para manter '{animal_para_editar.raça}'): ")
            nova_cor = input(f"Nova cor (deixe em branco para manter '{animal_para_editar.cor}'): ")

            if nova_raca:
                animal_para_editar.raça = nova_raca
            if nova_cor:
                animal_para_editar.cor = nova_cor
            print(f"'{animal_para_editar.nome}' atualizado: {animal_para_editar.info()}")
        else:
            print(f"Animal '{nome_edicao}' não encontrado.")

    elif opcao == "4": # Remover Animal
        nome_remover = input("Digite o nome do animal para remover: ")
        animal_para_remover = encontrar_animal(nome_remover, lista_de_animais)
        if animal_para_remover:
            lista_de_animais.remove(animal_para_remover)
            print(f"Animal '{nome_remover}' removido com sucesso.")
        else:
            print(f"Animal '{nome_remover}' não encontrado.")

    elif opcao == "5": # Listar Todos os Animais
        listar_animais(lista_de_animais)

    elif opcao == "6": # Sair
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")