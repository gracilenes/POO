class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida
    def mostrar_vida(self):
        return self.__vida

class Pontuacao:
    def __init__(self):
        self.__pontos = 0
        def adicionar_pontos(self, valor):
            if valor > 0:
                self.__pontos += valor
    def mostrar_pontos(self):
        return self.__pontos

class Inimigo:
    def __init__(self, nome, forca):
        self.nome = nome
        self.__forca = forca
    def get_forca(self):
        return self.__forca
    def atacar(self):
        print(f"{self.nome} ataca com força {self.get_forca()}!")

