class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado
       
    def get_saldo(self):
        return self.__saldo
       
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False
    
class ProcessadorImagem:
    def __init__(self, imagem):
        self.imagem = imagem
        self.__formato_original = self.__detectar_formato()
   
    def __detectar_formato(self):
        if self.imagem.endswith('.jpg'):
            return 'JPEG'
        elif self.imagem.endswith('.png'):
            return 'PNG'
        elif self.imagem.endswith('.gif'):
            return 'GIF'
        else:
            return 'Desconhecido'
    def obter_informacoes(self):
        return {
            "arquivo": self.imagem,
            "formato": self.__formato_original,
        }
