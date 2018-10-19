# Classe Aluno
# Importando a classe Pessoa
from Pessoa import Pessoa

class Aluno(Pessoa):
    # Método Construtor
    def __init__(self, nome, cpf, idade, matricula, curso):
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.curso = curso

    # Sobrescrever o método str
    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}, Idade: {self.idade}, Matrícula: {self.matricula}, Curso: {self.curso}'