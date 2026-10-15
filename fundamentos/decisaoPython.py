class Idade():
    def __init__(self):
        self.idade = int(input("Digite sua idade: "))
        if self.idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")

if __name__ == '__main__':
    minha_idade = Idade()
