class Pessoa:
    def __init__(self):
        self.__nome = "gracilene"
        self.__idade = 18

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            print("Idade não pode ser negativa.")


pessoa1 = Pessoa()

pessoa1.nome = 'jales'
pessoa1.idade =  16

print(pessoa1.nome)
print(pessoa1.idade)