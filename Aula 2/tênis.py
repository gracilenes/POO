class Tenis:
    def __init__(self):
        self.nome = None
        self.preco = None
        self.tamanho = None
        self.cor = None
        self.modalidade = None
    def aumentar_quantidade(self, quantidade):
        self.quantidade += quantidade
       
tenis1 = Tenis()

tenis1.quantidade = 5
print(tenis1.quantidade)

tenis1.aumentar_quantidade(15)
print(tenis1.quantidade)



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


