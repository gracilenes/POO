class Tenis:
    def __init__(self):
        self.nome = None
        self.preco = None
        self.tamanho = None
        self.cor = None
        self.modalidade = None
    def aumentar_quantidade(self, quantidade):
        self.quantidade += quantidade

    def remover_quantidade(self, quantidade):
        self.quantidade -= quantidade

    def desconto(self, porcentagem):
        self.preco -= self.preco * porcentagem / 100
       
tenis1 = Tenis()

tenis1.quantidade(10)
print(tenis1.quantidade)

tenis1.aumentar_quantidade(15)
print(tenis1.quantidade)

tenis1.remover_quantidade(4)
print(tenis1.quantidade) 

tenis1.desconto(20)
print(tenis1.desconto)



class Livro:
    def __init__(self):
        self.tipo = None
        self.capa = None
        self.titulo = None
        self.preco = None
        self.cor = None

livro1 = Livro()
livro1.nome = "Lute contra os medos, Supere as ingeruranças, Reaja e volte a ser feliz"
print(livro1.nome)


