class Livro():
    def __init__(self,titulo, autor, paginas = 100):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
livro1 = Livro("Python Básico", "João Silva", 250)
livro2 = Livro("Aprendendo Lógica", "Maria Souza")

print("Livro 1")
print(livro1.titulo)
print(livro1.autor)
print(livro1.paginas)

print("Livro 2")
print(livro2.titulo)
print(livro2.autor)
print(livro2.paginas)
