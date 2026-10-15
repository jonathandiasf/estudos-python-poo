import random
import json
import os # Para verificar se o arquivo existe

# Classe base para Pessoa
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf
        }

# --- Bank Account Classes ---
class ContaBancaria:
    banco = "PyBank"

    def __init__(self, nome_titular, saldo_inicial=0, agencia=None, conta=None):
        self.nome_titular = nome_titular
        self._saldo = saldo_inicial  # Internal balance shared with account subclasses
        self.agencia = agencia if agencia else random.randint(1000, 9999)
        self.conta = conta if conta else random.randint(100000, 999999)

    def __str__(self):
        return f"Conta {self.banco} - Titular: {self.nome_titular}, Agência: {self.agencia}, Conta: {self.conta}, Saldo: R${self._saldo:.2f}"

    def titularConta(self):
        """Returns the name of the account holder."""
        return self.nome_titular

    def depositar(self, valor):
        """Deposits a given amount into the account."""
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self._saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        """Withdraws a given amount from the account."""
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
            return False
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self._saldo:.2f}")
            return True
        else:
            print("Saldo insuficiente para realizar o saque.")
            return False

    def transferir(self, conta_destino, valor):
        """Transfers a given amount to another bank account."""
        if self.sacar(valor): # Reusing sacar logic (Abstraction/Code Reusability)
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para conta {conta_destino.conta} realizada com sucesso.")
            return True
        else:
            print("Transferência não realizada: saldo insuficiente ou valor inválido.")
            return False

    def consultar_saldo(self):
        """Returns the current balance of the account."""
        return self._saldo

    def to_dict(self):
        """Converts the account object to a dictionary for JSON serialization."""
        return {
            "nome_titular": self.nome_titular,
            "agencia": self.agencia,
            "conta": self.conta,
            "saldo": self._saldo
        }
# --- Subclasses for Specific Account Types ---
class ContaCorrente(ContaBancaria):
    def __init__(self, nome_titular, saldo_inicial=0, limite=1000, agencia=None, conta=None):
        super().__init__(nome_titular, saldo_inicial, agencia, conta)
        self.limite = limite

    def sacar(self, valor):
        """Withdraws amount, considering overdraft limit."""
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
            return False
        if self._saldo + self.limite >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo (c/ limite): R${self._saldo:.2f}")
            return True
        else:
            print("Saldo insuficiente e limite excedido para realizar o saque.")
            return False

    def __str__(self):
        return f"Conta Corrente {self.banco} - Titular: {self.nome_titular}, Agência: {self.agencia}, Conta: {self.conta}, Saldo: R${self._saldo:.2f}, Limite: R${self.limite:.2f}"

    def to_dict(self):
        data = super().to_dict()
        data["tipo_conta"] = "corrente"
        data["limite"] = self.limite
        return data
# --- Subclass for Savings Account ---
class ContaPoupanca(ContaBancaria):
    def __init__(self, nome_titular, saldo_inicial=0, taxa_rendimento=0.005, agencia=None, conta=None):
        super().__init__(nome_titular, saldo_inicial, agencia, conta)
        self.taxa_rendimento = taxa_rendimento

    def render_juros(self):
        """Applies interest to the savings account."""
        juros = self._saldo * self.taxa_rendimento
        self.depositar(juros)
        print(f"Juros de R${juros:.2f} aplicados. Novo saldo: R${self._saldo:.2f}")

    def __str__(self):
        return f"Conta Poupança {self.banco} - Titular: {self.nome_titular}, Agência: {self.agencia}, Conta: {self.conta}, Saldo: R${self._saldo:.2f}, Taxa Rendimento: {self.taxa_rendimento*100:.2f}%"

    def to_dict(self):
        data = super().to_dict()
        data["tipo_conta"] = "poupanca"
        data["taxa_rendimento"] = self.taxa_rendimento
        return data

class Banco:
    def __init__(self, nome="PyBank", filename="bank_data.json"):
        self.nome = nome
        self.clientes = [] # List to store Pessoa objects, each potentially holding accounts
        self.filename = filename
        self.load_data() # Load data when bank is initialized

    def adicionar_cliente(self, cliente):
        """Adds a client to the bank."""
        # Check if client (by CPF) already exists
        if any(c.cpf == cliente.cpf for c in self.clientes):
            print(f"Erro: Cliente com CPF {cliente.cpf} já existe.")
            return False
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado com sucesso.")
        return True

    def encontrar_cliente_por_cpf(self, cpf):
        """Finds a client by CPF."""
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def encontrar_conta_por_numero(self, numero_conta):
        """Finds an account by its number across all clients."""
        for cliente in self.clientes:
            for conta in cliente.contas: # Assuming Cliente can have multiple accounts
                if conta.conta == numero_conta:
                    return conta
        return None

    def listar_clientes(self):
        """Lists all clients and their accounts."""
        if not self.clientes:
            print("Não há clientes cadastrados no banco.")
            return

        print("\n--- Clientes do Banco ---")
        for cliente in self.clientes:
            print(f"\n{cliente}")
            if hasattr(cliente, 'contas') and cliente.contas:
                print("  Contas:")
                for conta in cliente.contas:
                    print(f"    - {conta}")
            else:
                print("  (Sem contas associadas)")
        print("-------------------------")

    def save_data(self):
        """Saves all bank data (clients and their accounts) to a JSON file."""
        data = {
            "clientes": []
        }
        for cliente in self.clientes:
            cliente_data = cliente.to_dict()
            if hasattr(cliente, 'contas'):
                cliente_data["contas"] = [conta.to_dict() for conta in cliente.contas]
            data["clientes"].append(cliente_data)

        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Dados do banco salvos em '{self.filename}'.")

    def load_data(self):
        """Loads bank data from a JSON file."""
        if not os.path.exists(self.filename):
            print(f"Arquivo '{self.filename}' não encontrado. Iniciando com banco vazio.")
            return

        with open(self.filename, 'r') as f:
            data = json.load(f)

        self.clientes = []
        for cliente_data in data.get("clientes", []):
            # Reconstruct Pessoa object
            cliente = Pessoa(cliente_data["nome"], cliente_data["cpf"])
            cliente.contas = [] # Prepare for accounts

            for conta_data in cliente_data.get("contas", []):
                # Reconstruct ContaBancaria or its subclasses
                if conta_data.get("tipo_conta") == "corrente":
                    conta = ContaCorrente(
                        conta_data["nome_titular"],
                        conta_data["saldo"],
                        conta_data["limite"],
                        conta_data["agencia"],
                        conta_data["conta"]
                    )
                elif conta_data.get("tipo_conta") == "poupanca":
                     conta = ContaPoupanca(
                        conta_data["nome_titular"],
                        conta_data["saldo"],
                        conta_data["taxa_rendimento"],
                        conta_data["agencia"],
                        conta_data["conta"]
                    )
                else: # Default to generic ContaBancaria if type not specified
                    conta = ContaBancaria(
                        conta_data["nome_titular"],
                        conta_data["saldo"],
                        conta_data["agencia"],
                        conta_data["conta"]
                    )
                cliente.contas.append(conta)
            self.clientes.append(cliente)
        print(f"Dados do banco carregados de '{self.filename}'.")
# --- Client Class ---
class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.contas = [] # A client can have multiple accounts (composition)

    def adicionar_conta(self, conta):
        """Adds a bank account to the client."""
        self.contas.append(conta)
        print(f"Conta {conta.conta} adicionada para o cliente {self.nome}.")

    def to_dict(self):
        data = super().to_dict()
        # Accounts are handled in Banco.save_data for simplicity, or could be included here
        # data["contas"] = [conta.to_dict() for conta in self.contas]
        return data
# --- Main Program ---
def main():
    meu_banco = Banco() # Initializes and tries to load data

    while True:
        print("\n--- Menu do PyBank ---")
        print("1. Adicionar Novo Cliente")
        print("2. Criar Conta para Cliente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Transferir")
        print("6. Consultar Saldo")
        print("7. Listar Clientes e Contas")
        print("8. Aplicar Rendimento (Poupança)")
        print("9. Salvar Dados e Sair")
        print("0. Sair sem Salvar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            novo_cliente = Cliente(nome, cpf)
            meu_banco.adicionar_cliente(novo_cliente)
        elif opcao == '2':
            cpf = input("CPF do cliente para adicionar conta: ")
            cliente = meu_banco.encontrar_cliente_por_cpf(cpf)
            if cliente:
                print("Tipo de conta: (1) Corrente, (2) Poupança")
                tipo = input("Escolha o tipo de conta: ")
                saldo_inicial = float(input("Saldo inicial: R$"))
                if tipo == '1':
                    nova_conta = ContaCorrente(cliente.nome, saldo_inicial)
                elif tipo == '2':
                    nova_conta = ContaPoupanca(cliente.nome, saldo_inicial)
                else:
                    print("Tipo de conta inválido.")
                    continue
                cliente.adicionar_conta(nova_conta)
            else:
                print("Cliente não encontrado.")
        elif opcao == '3':
            num_conta = int(input("Número da conta para depósito: "))
            conta = meu_banco.encontrar_conta_por_numero(num_conta)
            if conta:
                valor = float(input("Valor a depositar: R$"))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")
        elif opcao == '4':
            num_conta = int(input("Número da conta para saque: "))
            conta = meu_banco.encontrar_conta_por_numero(num_conta)
            if conta:
                valor = float(input("Valor a sacar: R$"))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")
        elif opcao == '5':
            num_conta_origem = int(input("Número da conta de origem: "))
            conta_origem = meu_banco.encontrar_conta_por_numero(num_conta_origem)
            if conta_origem:
                num_conta_destino = int(input("Número da conta de destino: "))
                conta_destino = meu_banco.encontrar_conta_por_numero(num_conta_destino)
                if conta_destino:
                    valor = float(input("Valor a transferir: R$"))
                    conta_origem.transferir(conta_destino, valor)
                else:
                    print("Conta de destino não encontrada.")
            else:
                print("Conta de origem não encontrada.")
        elif opcao == '6':
            num_conta = int(input("Número da conta para consultar saldo: "))
            conta = meu_banco.encontrar_conta_por_numero(num_conta)
            if conta:
                print(f"Saldo da conta {conta.conta}: R${conta.consultar_saldo():.2f}")
            else:
                print("Conta não encontrada.")
        elif opcao == '7':
            meu_banco.listar_clientes()
        elif opcao == '8':
            num_conta = int(input("Número da conta poupança para render juros: "))
            conta = meu_banco.encontrar_conta_por_numero(num_conta)
            if isinstance(conta, ContaPoupanca):
                conta.render_juros()
            elif conta:
                print("Esta não é uma conta poupança.")
            else:
                print("Conta não encontrada.")
        elif opcao == '9':
            meu_banco.save_data()
            print("Saindo do PyBank. Até mais!")
            break
        elif opcao == '0':
            print("Saindo do PyBank sem salvar. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
# end of main()
if __name__ == '__main__':
    main()