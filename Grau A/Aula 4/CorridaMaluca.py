import random

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.posicao = 0

    def atualizar(self):
        dado = random.randint(1, 6)
        self.posicao += dado
        if self.posicao % 5 == 0:
            self.posicao -= 1
        elif self.posicao == 7 or self.posicao == 17:
            self.posicao += 2
        elif self.posicao == 13:
            self.posicao = 0
        elif self.posicao > 20:
            self.posicao = 20

    def getPos(self):
        return self.posicao

print('Corrida Maluca 😵')
input('Pressione enter para começar')

competidores = []
competidores.append(Competidor('Competidor 1'))
competidores.append(Competidor('Competidor 2'))
competidores.append(Competidor('Competidor 3'))
competidores.append(Competidor('Competidor 4'))
competidores.append(Competidor('Competidor 5'))

vencedor = None
while not vencedor:
    for i in competidores:
        i.atualizar()
        if i.getPos() >= 20:
            vencedor = i.nome
            break
    for i in competidores:
        print(f'{i.nome}: {i.getPos()}')
    print('|-|-|-|-|-|-|-|-|-|-|')

print(f'O vencedor da corrida é {vencedor}!')
