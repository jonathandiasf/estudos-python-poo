class Produto:
    # Atributos privados
    def __init__(self, nome, preco, quantidade=0):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    # Métodos Getters e Setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    # Método setter para o preço ser devidamente válido
    @preco.setter
    def preco(self, preco):
        if preco > 0:
            self.__preco = preco
        else:
            print("Preço inválido! Deve ser maior que 0.")

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            print("Quantidade inválida! Deve ser maior ou igual a 0.")


class GerenciadorEstoque:
    def __init__(self):
        # Inicializando com alguns produtos de exemplo (convertendo preços para float e quantidades para int)
        self.lista_produtos = [
            Produto("Arroz", 15.00, 10),
            Produto("Feijão", 9.00, 13),
            Produto("Macarrão", 4.00, 20)
        ]

    def adicionar_produto(self, nome, preco, quantidade):
        novo_produto = Produto(nome, preco, quantidade)
        self.lista_produtos.append(novo_produto)
        print("Produto adicionado com sucesso!")

    def remover_produto(self, nome):
        for produto in self.lista_produtos:
            if produto.nome.lower() == nome.lower():
                self.lista_produtos.remove(produto)
                return True
        return False

    def atualizar_produto(self, nome, novo_nome, novo_preco, nova_quantidade):
        for produto in self.lista_produtos:
            if produto.nome.lower() == nome.lower():
                produto.nome = novo_nome
                produto.preco = novo_preco
                produto.quantidade = nova_quantidade
                return True
        return False

    def consultar_produto(self, nome):
        for produto in self.lista_produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        return None

    def listar_produtos(self):
        if not self.lista_produtos:
            print("Nenhum produto cadastrado.")
            return
        for produto in self.lista_produtos:
            print(f"Nome: {produto.nome} | Preço: R$ {produto.preco:.2f} | Quantidade: {produto.quantidade}")


# Fluxo principal do programa
gerenciador = GerenciadorEstoque()

while True:
    print("\n--- Sistema de Gerenciamento de Estoque ---")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar produto")
    print("4 - Consultar produto")
    print("5 - Listar produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        try:
            preco = float(input("Digite o preço do produto: ").replace(",", "."))
            quantidade = int(input("Digite a quantidade do produto: "))
            gerenciador.adicionar_produto(nome, preco, quantidade)
        except ValueError:
            print("Erro: Preço ou quantidade inválidos. Digite valores numéricos válidos.")

    elif opcao == "2":
        nome = input("Digite o nome do produto a ser removido: ")
        if gerenciador.remover_produto(nome):
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado!")

    elif opcao == "3":
        nome = input("Digite o nome do produto a ser atualizado: ")
        novo_nome = input("Digite o novo nome do produto: ")
        try:
            novo_preco = float(input("Digite o novo preço do produto: ").replace(",", "."))
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            if gerenciador.atualizar_produto(nome, novo_nome, novo_preco, nova_quantidade):
                print("Produto atualizado com sucesso!")
            else:
                print("Produto não encontrado!")
        except ValueError:
            print("Erro: Preço ou quantidade inválidos.")

    elif opcao == "4":
        nome = input("Digite o nome do produto a ser consultado: ")
        produto = gerenciador.consultar_produto(nome)
        if produto:
            print("\nProduto encontrado:")
            print(f"Nome: {produto.nome}")
            print(f"Preço: R$ {produto.preco:.2f}")
            print(f"Quantidade: {produto.quantidade}")
        else:
            print("Produto não encontrado!")

    elif opcao == "5":
        print("\nLista de produtos:")
        gerenciador.listar_produtos()

    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")