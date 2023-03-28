import random
from time import sleep

class Competidor:
    def __init__(self, nome):
        self.nome = nome #nome
        self.pos = 0 #posição 

    def atualizar(self): #atualizar o dado
        dado = random.randint(1, 6)
        self.pos += dado
        if self.pos % 5 == 0:
            self.pos -= 1
        elif self.pos == 7 or self.pos == 17:
            self.pos += 2
        elif self.pos == 13:
            self.pos = 0
        elif self.pos > 20:
            self.pos = 20

    def getPos(self):
        return self.pos

print('Corrida Maluca 😵')
input('Pressione enter para começar')

competidores = []
competidores.append(Competidor('Competidor 1'))
competidores.append(Competidor('Competidor 2'))
competidores.append(Competidor('Competidor 3'))
competidores.append(Competidor('Competidor 4'))
competidores.append(Competidor('Competidor 5'))

vencedor = None
while not vencedor: #vencedor
    for i in competidores:
        i.atualizar()
        if i.getPos() >= 20:
            vencedor = i.nome
            break
    for i in competidores:
        print(f'{i.nome}: {i.getPos()}')
    print('|-|-|-|-|-|-|-|-|-|-|')

print('O vencedor da corrida é...')
sleep(2)
print(f'{vencedor}!')
