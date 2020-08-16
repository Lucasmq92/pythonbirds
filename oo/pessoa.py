class Pessoa:
    def __init__(self,nome=None,idade=27):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return f'Olá id{self}'

if __name__ == '__main__':
    p = Pessoa('Lucas')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())     #implicitamente, passa p como parâmetro, assim como qualquer método que use
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)
    print(p.idade)

"""
To import in Python Console:
from oo.pessoa import Pessoa
"""