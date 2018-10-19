# Classe Funcionario
# Importando a classe Pessoa
from Pessoa import Pessoa

class Funcionario(Pessoa):
    # Método Contrutor
    def __init__(self, nome, cpf, idade, matricula, salario, setor):
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.salario = salario
        self.setor = setor

    # Sobrescrever o método str
    def __str__(self):
        return f'{super().__str__()}, Matricula: {self.matricula}, Salário: {self.salario}, Setor: {self.setor}'
