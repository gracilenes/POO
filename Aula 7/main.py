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

biblioteca = Biblioteca("Livros")
biblioteca.adicionar_categoria("Membros")
biblioteca.adicionar_categoria("Empréstimos")

class Livros:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestimos = []

    def adicionar_emprestimos(self, emprestimo):
        self.emprestimos.append(emprestimo)

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

class Emprestimo:
    def __init__(self, livro, membro):
        self.livro = livro
        self.membro = membro
        livro.adicionar_emprestimo(self)
        membro.adicionar_emprestimo(self)

class Biblioteca:
    def __init__(self):
        self.membros = []

    def adicionar_membro(self, membro):
        self.membros.append(membro)

livro1 = Livros("Lute Supere e Reaja")
livro2 = Livros("Mary Jane")

membro1 = Membro("Gracilene")
membro2 = Membro("Carlos")

biblioteca = Biblioteca()
biblioteca.adicionar_membro(membro1)
biblioteca.adicionar_membro(membro2)

emprestimo1 = Emprestimo(livro1, membro1)
emprestimo2 = Emprestimo(livro2, membro1)
emprestimo3 = Emprestimo(livro1, membro2)
