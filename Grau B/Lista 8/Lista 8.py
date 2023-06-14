import random

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def exibirDescricao(self):
        print("Este é um animal chamado", self.nome)

class Carnivoro(Animal):
    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal carnívoro.")
    
    def caca(self):
        print("O animal carnívoro está caçando.")

class Herbivoro(Animal):
    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal herbívoro.")
    
    def pastar(self):
        print("O animal herbívoro está pastando.")

class Onivoro(Carnivoro, Herbivoro):
    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal onívoro.")
    
    def comer(self):
        escolha = random.randint(0, 1)
        if escolha == 0:
            self.caca()
        else:
            self.pastar()

leao = Carnivoro("Leão")
leao.exibirDescricao()
leao.caca()

vaca = Herbivoro("Vaca")
vaca.exibirDescricao()
vaca.pastar()

urso = Onivoro("Urso")
urso.exibirDescricao()
urso.comer()
