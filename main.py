# Arquivo Principal
from Pessoa import Pessoa
from Funcionario import Funcionario
# Criando os objetos
p1 = Pessoa('João', '123', 20)

# Pegando informações do objeto
print(p1.get_nome())
print(p1.get_cpf())
print(p1.get_idade())

# Objeto em versão texto
print(p1)

'''
Método de Herança entre classes:
    > Classe A: Mãe 
    > Classe B: Filha
    > A Classe filha HERDA (Ganha de graça) todos os atributos e métodos da classe mãe, além de poder criar novos 
    métodos e atributos para a mesma.
'''

# Objeto funcionário
f1 = Funcionario('José', '456', 10, '0099', 2526.45, 'Biblioteca')

print(f1.get_nome())
print(f1)

# Criar classe Aluno e classe Professor
