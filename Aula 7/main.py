# Biblioteca precisar de um sistema para gerenciar

class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.categorias = []
    
    def adicionar_categoria(self, nome_categoria):
        categoria = Categoria(nome_categoria)
        self.categorias.append(Categoria)

print = Biblioteca("Livros")
print.adicionar_categoria("Membros")
print.adicionar_categoria("Empréstimos")