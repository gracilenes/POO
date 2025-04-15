class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__idade = 0

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            print("Idade não pode ser negativa.")