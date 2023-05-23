class SerVivo:
    def __init__(self, nome):
        self.__nome = nome
        self.__nomeCientifico = ""
        self.__filo = ""
        self.__classe = ""
        self.__familia = ""
        self.__genero = ""
        self.__especie = ""
        self.__estadoconservacao = 0

    def getNome(self):
        return self.__nome


class Animal(SerVivo):
    def __init__(self, nome):
        super().__init__(nome)


class Vegetal(SerVivo):
    def __init__(self, nome):
        super().__init__(nome)


class Bioma:
    def __init__(self, nome):
        self.__nome = nome
        self.__fauna = []
        self.__flora = []

    def getNome(self):
        return self.__nome

    def adicionarAnimal(self, animal):
        self.__fauna.append(animal)

    def adicionarVegetal(self, vegetal):
        self.__flora.append(vegetal)

    def exibirFauna(self):
        print(" - Fauna: - ")
        for animal in self.__fauna:
            print(animal.getNome())

    def exibirFlora(self):
        print(" - Flora: - ")
        for vegetal in self.__flora:
            print(vegetal.getNome())


bioma1 = Bioma("Amazônia")
bioma2 = Bioma("Mata Atlântica")
bioma3 = Bioma("Cerrado")
bioma4 = Bioma("Caatinga")
bioma5 = Bioma("Pampa")
bioma6 = Bioma("Pantanal")

lista_biomas = [bioma1, bioma2, bioma3, bioma4, bioma5, bioma6]

faunaBR = [
    # [Animal	Amazônia Mata Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Capivara', True, True, True, True, True, True],
    ['Gralha azul', False, True, False, False, True, False],
    ['Tamanduá-bandeira', True, True, True, False, True, False],
    ['Onça pintada', True, True, False, True, False, True],
    ['Tatu-bola', False, False, False, True, False, False]
]

floraBR = [
    # [Planta	Amazônia Mata Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Ipê amarelo', True, True, True, True, True, True],
    ['Araucária', False, True, False, False, True, False],
    ['Mandacaru', False, False, True, True, False, False],
    ['Vitória-régia', True, False, False, False, False, True],
    ['Jatobá', True, True, True, False, False, True]

]

for animal in faunaBR:
    nome_animal = animal[0]

    for i in range(1, len(animal)):
        if animal[i]:
            nome_bioma = lista_biomas[i - 1].getNome()
            bioma = None
            for b in lista_biomas:
                if b.getNome() == nome_bioma:
                    bioma = b
                    break

            obj_animal = Animal(nome_animal)


            bioma.adicionarAnimal(obj_animal)

for planta in floraBR:
    nome_planta = planta[0]

    for i in range(1, len(planta)):
        if planta[i]:
            nome_bioma = lista_biomas[i - 1].getNome()
            bioma = None
            for b in lista_biomas:
                if b.getNome() == nome_bioma:
                    bioma = b
                    break

            obj_planta = Vegetal(nome_planta)
            bioma.adicionarVegetal(obj_planta)

print('Lista de Biomas:')
for bioma in lista_biomas:
    print(bioma.getNome())

print('\nLista de Fauna e Flora por Bioma:')
for bioma in lista_biomas:
    print("\nBioma:", bioma.getNome())
    bioma.exibirFauna()
    bioma.exibirFlora()