class Turma():
    def __init__(self, *alunos):
        self.alunos = list(alunos)
    def listar(self):
        """
        exibe a lista 
        """
        for aluno in self.alunos:
            print(aluno) 

turma1 = Turma("Ana", "Bruno", "Carlos")
turma2 = Turma("Larissa")       

turma1.listar()
turma2.listar()