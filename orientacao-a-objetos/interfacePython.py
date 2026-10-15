from abc import ABC, abstractmethod

# 1. Definição da Interface (Classe Abstrata Pura)
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        """Método que todas as classes filhas devem implementar."""
        pass

# 2. Implementações concretas da Interface (Polimorfismo)
class NotificadorEmail(Notificador):
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando E-mail: {mensagem}")

class NotificadorSMS(Notificador):
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando SMS: {mensagem}")

class NotificadorPush(Notificador):
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando Notificação Push: {mensagem}")

# 3. Função que demonstra o Polimorfismo
# Ela não precisa saber o tipo exato da classe, apenas que ela implementa a interface 'Notificador'
def comunicar_usuario(notificador: Notificador, msg: str):
    notificador.enviar(msg)

# --- Demonstração ---
# Criando os objetos diferentes
email = NotificadorEmail()
sms = NotificadorSMS()
push = NotificadorPush()

# Chamando o mesmo comportamento de formas diferentes (Polimorfismo)
comunicar_usuario(email, "Seu código de ativação chegou!")
comunicar_usuario(sms, "Seu código de ativação chegou!")
comunicar_usuario(push, "Seu código de ativação chegou!")