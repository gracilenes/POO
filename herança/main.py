class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Departamento: {self.departamento}")

