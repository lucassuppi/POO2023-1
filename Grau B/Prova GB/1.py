import os
os.system('cls')

class CorpoCeleste:
    def __init__(self, nome, diametro, composicao):
        self.nome = nome
        self.diametro = diametro
        self.composicao = composicao

    def exibirInformacoes(self):
        os.system('cls')
        print("Nome:", self.nome)
        print("Diâmetro:", self.diametro, "km")
        print("Composição:", self.composicao)

class Planeta(CorpoCeleste):
    def __init__(self, nome, diametro, composicao, numLuas, tipoAtmosfera):
        CorpoCeleste.__init__(self, nome, diametro, composicao)
        self.numLuas = numLuas
        self.tipoAtmosfera = tipoAtmosfera

    def exibirInformacoes(self):
        CorpoCeleste.exibirInformacoes(self)
        print("Número de Luas:", self.numLuas)
        print("Tipo de Atmosfera:", self.tipoAtmosfera)
        print('')


class Satelite(CorpoCeleste):
    def __init__(self, nome, diametro, composicao, planetaOrbita, periodoOrbita):
        CorpoCeleste.__init__(self, nome, diametro, composicao)
        self.planetaOrbita = planetaOrbita
        self.periodoOrbita = periodoOrbita

    def exibirInformacoes(self):
        CorpoCeleste.exibirInformacoes(self)
        print("Planeta de Órbita:", self.planetaOrbita)
        print("Período de Órbita:", self.periodoOrbita)
        print('')

class Estrela(CorpoCeleste):
    def __init__(self, nome, diametro, composicao, temperatura, tipoEspectral):
        CorpoCeleste.__init__(self, nome, diametro, composicao)
        self.temperatura = temperatura
        self.tipoEspectral = tipoEspectral

    def exibirInformacoes(self):
        CorpoCeleste.exibirInformacoes(self)
        print("Temperatura:", self.temperatura, "C")
        print("Tipo Espectral:", self.tipoEspectral)
        print('')

corposCelestes = []

planeta1 = Planeta("Vênus", 1000, "rochas", 10, "carbono")
corposCelestes.append(planeta1)
satelite1 = Satelite("Lua", 3000, "rochas", "terra", 25)
corposCelestes.append(satelite1)
estrela1 = Estrela("Sol", 150000, "plasma", 5000, "plasma")
corposCelestes.append(estrela1)

while True:
    print("Escolha uma das opções abaixo:")
    print("1 - Exibir informações dos corpos celestes")
    print("2 - Fechar programa")
    escolha = int(input())

    if escolha == 1:
        os.system('cls')
        print("Escolha um dos corpos celestes abaixo:")
        for i, corpo in enumerate(corposCelestes):
            print(i+1, "-", corpo.nome)
        escolha_corpo = int(input())

        if escolha_corpo > 0 and escolha_corpo <= len(corposCelestes):
            corpoSelecionado = corposCelestes[escolha_corpo-1]
            corpoSelecionado.exibirInformacoes()
        else:
            print("Opção inválida")
    elif escolha == 2:
        break
    else:
        print("Opção inválida")