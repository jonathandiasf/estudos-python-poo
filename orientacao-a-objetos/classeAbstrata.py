from abc import ABC, abstractmethod

# ==========================================
# 1. INTERFACE (Contrato Puro)
# Em Python, criamos interfaces usando ABC onde TODOS os métodos são abstratos
# e a classe não possui estado (atributos de instância) ou implementação.
# ==========================================
class Autenticavel(ABC):
    @abstractmethod
    def login(self) -> bool:
        """Interface: define apenas a assinatura do método. Sem implementação."""
        pass

    @abstractmethod
    def logout(self) -> None:
        pass

# ==========================================
# 2. CLASSE ABSTRATA (Molde/Modelo com Herança e Estado)
# Pode conter métodos abstratos (que devem ser implementados pelas subclasses)
# E também métodos concretos (com lógica compartilhada) e atributos de estado.
# ==========================================
class Funcionario(ABC):
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base  # Estado compartilhado

    @abstractmethod
    def calcular_salario(self) -> float:
        """Método abstrato: cada subclasse define sua própria regra de cálculo."""
        pass

    def obter_detalhes(self) -> str:
        """Método concreto: herdado diretamente pelas subclasses sem necessidade de reescrita."""
        return f"Funcionário: {self.nome} | Salário Base: R$ {self.salario_base:.2f}"

# ==========================================
# 3. IMPLEMENTAÇÃO / HERANÇA
# ==========================================

# Gerente herda de Funcionario (Classe Abstrata) E implementa Autenticavel (Interface)
class Gerente(Funcionario, Autenticavel):
    def __init__(self, nome: str, salario_base: float, bonus: float):
        super().__init__(nome, salario_base)
        self.bonus = bonus
        self._logado = False

    # Implementação obrigatória do método abstrato de Funcionario
    def calcular_salario(self) -> float:
        return self.salario_base + self.bonus

    # Implementações obrigatórias da Interface Autenticavel
    def login(self) -> bool:
        self._logado = True
        print(f"Gerente {self.nome} logou no sistema.")
        return self._logado

    def logout(self) -> None:
        self._logado = False
        print(f"Gerente {self.nome} deslogou.")

# Auxiliar apenas herda de Funcionario (Não precisa de autenticação)
class Auxiliar(Funcionario):
    # Implementação obrigatória do método abstrato de Funcionario
    def calcular_salario(self) -> float:
        return self.salario_base

# ==========================================
# Execução e Teste das Regras
# ==========================================
if __name__ == "__main__":
    # Criando instâncias das classes concretas
    gerente = Gerente("Alice", 8000.0, 2000.0)
    auxiliar = Auxiliar("Bruno", 2500.0)

    # 1. Testando Herança da Classe Abstrata (Método Concreto e Abstrato)
    print(gerente.obter_detalhes())
    print(f"Salário Total Gerente: R$ {gerente.calcular_salario():.2f}\n")

    print(auxiliar.obter_detalhes())
    print(f"Salário Total Auxiliar: R$ {auxiliar.calcular_salario():.2f}\n")

    # 2. Testando comportamento da Interface
    gerente.login()
    gerente.logout()

    # 3. Regra do Modelo: Não é possível instanciar classes abstratas ou interfaces diretamente
    try:
        f = Funcionario("Invalido", 1000)  # Gera erro
    except TypeError as e:
        print(f"\n[ERRO ESPERADO]: Não foi possível instanciar Funcionario: {e}")