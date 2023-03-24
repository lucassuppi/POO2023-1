import random

class DadoVirtual():
    def __init__(self, num_faces):
        self.num_faces = num_faces

    def jogardado(self):
        jogadas = []
        for i in range(3):
            jogada = random.randint(1, self.num_faces)
            jogadas.append(jogada)
        return jogadas
    
dado6 = DadoVirtual(6)
print(f'Jogando dado com 6 lados: {dado6.jogardado()}')

dado8 = DadoVirtual(8)
print(f'Jogando dado com 8 lados: {dado8.jogardado()}')

dado12 = DadoVirtual(12)
print(f'Jogando dado com 12 lados: {dado12.jogardado()}')