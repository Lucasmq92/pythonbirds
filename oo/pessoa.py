class Pessoa:

    olhos = 2

    def __init__(self,*filhos,nome=None,idade=27):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá id{self}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def metodo_classe(cls):
        return f'{cls} olhos: {cls.olhos}'

if __name__ == '__main__':
    lucas = Pessoa(nome='Lucas de Moura Quadros',idade=27)
    yago = Pessoa(nome='Yago de Moura Quadros',idade=26)
    laura = Pessoa(nome='Laura Quadros',idade=16)
    clarinha = Pessoa(nome='Maria Clara de Quadros',idade=5)
    luiz = Pessoa(lucas,yago,laura,clarinha,nome='Luiz Alberto de Quadros',idade=55)

    print("\nFilhos do Luiz:\n")
    for filho in luiz.filhos:
        print(filho.nome)

    lucas.olhos = 3
    print(Pessoa.olhos)
    print(lucas.__dict__)
    del lucas.olhos
    print(lucas.__dict__,lucas.olhos)
    Pessoa.olhos = 1
    print(lucas.__dict__,lucas.olhos)

    print(Pessoa.metodo_estatico(),lucas.metodo_estatico())
    print(Pessoa.metodo_classe(),lucas.metodo_classe())

"""
To import in Python Console:
from oo.pessoa import Pessoa
"""