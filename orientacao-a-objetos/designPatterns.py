print("O Factory Method é um padrão de projeto criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. No exemplo abaixo, vamos simular um sistema de notificações que suporta diferentes canais(SMS e E-mail)")

from abc import ABC, abstractmethod

# Produto Abstrato
class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        pass

# Produto Concreto 1
class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando E-mail com a mensagem: '{mensagem}'")

# Produto Concreto 2
class NotificacaoSMS(Notificacao):
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando SMS com a mensagem: '{mensagem}'")

# Criador Abstrato (Factory)
class CanalNotificacao(ABC):
    @abstractmethod
    def criar_notificacao(self) -> Notificacao:
        pass

    def disparar_alerta(self, mensagem: str) -> None:
        # Chama o factory method para criar o objeto do produto
        notificacao = self.criar_notificacao()
        # Usa o produto
        notificacao.enviar(mensagem)

# Criador Concreto 1
class CanalEmail(CanalNotificacao):
    def criar_notificacao(self) -> Notificacao:
        return NotificacaoEmail()

# Criador Concreto 2
class CanalSMS(CanalNotificacao):
    def criar_notificacao(self) -> Notificacao:
        return NotificacaoSMS()

print("\n--- Demonstração do padrão de projeto Factory Method ---")

def cliente_enviar_alerta(canal: CanalNotificacao, mensagem: str) -> None:
    canal.disparar_alerta(mensagem)

print("---Teste com Canal de E-mail---")
canal_email = CanalEmail()
cliente_enviar_alerta(canal_email, "Esta é uma notificação por e-mail.")

print("\n---Teste com Canal de SMS---")
canal_sms = CanalSMS()
cliente_enviar_alerta(canal_sms, "Esta é uma notificação por SMS.")