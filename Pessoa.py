# Classe Pessoa
class Pessoa:
    # Método construtivo
    def  __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    # Métodos 'get'
    def get_nome(self):
        return self.nome
    def get_cpf(self):
        return self.cpf
    def get_idade(self):
        return self.idade

    # Sobrescrever o método str
    def __str__(self):
        return f'Nome {self.nome}, CPF: {self.cpf}, Idade: {self.idade}'