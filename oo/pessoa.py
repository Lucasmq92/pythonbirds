class Pessoa:
    def __init__(self,*filhos,nome=None,idade=27):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá id{self}'

if __name__ == '__main__':
    lucas = Pessoa(nome='Lucas de Moura Quadros',idade=27)
    yago = Pessoa(nome='Yago de Moura Quadros',idade=26)
    laura = Pessoa(nome='Laura Quadros',idade=16)
    clarinha = Pessoa(nome='Maria Clara de Quadros',idade=5)
    luiz = Pessoa(lucas,yago,laura,clarinha,nome='Luiz Alberto de Quadros',idade=55)
    print("\nFilhos do Luiz:\n")
    for filho in luiz.filhos:
        print(filho.nome)
"""
To import in Python Console:
from oo.pessoa import Pessoa
"""