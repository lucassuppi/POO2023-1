import random, os

class Equipe:
    def __init__(self, nome, competidores):
        self.nome = nome
        self.vitorias = 0
        self.competidores = competidores

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.vitorias = 0

equipe1 = Equipe("Equipe 1", [Competidor("Competidor 1"), Competidor("Competidor 2"), Competidor("Competidor 3")])
equipe2 = Equipe("Equipe 2", [Competidor("Competidor 1"), Competidor("Competidor 2"), Competidor("Competidor 3")])

while equipe1.vitorias < 10 and equipe2.vitorias < 10:

    print(f"Rodada {equipe1.vitorias + equipe2.vitorias + 1}")

    print("Escolha o competidor para a Equipe 1:")
    for i in range(len(equipe1.competidores)):
        print(i+1, "-", equipe1.competidores[i].nome)
    escolha1 = int(input())

    print("Escolha o competidor para a Equipe 2:")
    for i in range(len(equipe2.competidores)):
        print(i+1, "-", equipe2.competidores[i].nome)
    escolha2 = int(input())

    if escolha1 and escolha2 in [1, 2, 3]:

        competidor1 = equipe1.competidores[escolha1-1]
        competidor2 = equipe2.competidores[escolha2-1]

        print('\n╠═════════════════════════════════════════════════╣')
        print(f"O competidor {competidor1.nome}, da Equipe 1, escolheu...")
        escolha_competidor1 = random.randint(0, 2)
        if escolha_competidor1 == 0:
            print("Pedra 🗿")
        elif escolha_competidor1 == 1:
            print("Papel 📝")
        else:
            print("Tesoura ✂️")
        print(f"O competidor {competidor2.nome}, da Equipe 2, escolheu...")
        escolha_competidor2 = random.randint(0, 2)
        if escolha_competidor2 == 0:
            print("Pedra 🗿")
        elif escolha_competidor2 == 1:
            print("Papel 📝")
        else:
            print("Tesoura ✂️")
        print('╠═════════════════════════════════════════════════╣\n')

        if escolha_competidor1 == escolha_competidor2:
            print("Empate! Novo round iniciando...")
        elif escolha_competidor1 == 0 and escolha_competidor2 == 2:
            competidor1.vitorias += 1
            equipe1.vitorias += 1
            print(f"O competidor {competidor1.nome}, da Equipe 1, venceu o round!\n")
        elif escolha_competidor1 == 2 and escolha_competidor2 == 0:
            competidor2.vitorias += 1
            equipe2.vitorias += 1
            print(f"O competidor {competidor2.nome}, da Equipe 2, venceu o round!\n")
        elif escolha_competidor1 > escolha_competidor2:
            competidor1.vitorias += 1
            equipe1.vitorias += 1
            print(f"O competidor {competidor1.nome}, da Equipe 1, venceu o round!\n")
        else:
            competidor2.vitorias += 1
            equipe2.vitorias += 1
            print(f"O competidor {competidor2.nome}, da Equipe 2, venceu o round!\n")

        if equipe1.vitorias != equipe2.vitorias:
            if equipe1.vitorias > equipe2.vitorias:
                print("Escolha o próximo competidor para a Equipe 2:")
                for i in range(len(equipe2.competidores)):
                    print(i+1, "-", equipe2.competidores[i].nome)
                escolha_proximo = int(input())
                if escolha_proximo in [1, 2, 3]:
                    equipe2.competidores = equipe2.competidores[escolha_proximo-1:escolha_proximo] + equipe2.competidores[:escolha_proximo-1] + equipe2.competidores[escolha_proximo:]
            else:
                print("Escolha o próximo competidor para a Equipe 1:")
                for i in range(len(equipe1.competidores)):
                    print(i+1, "-", equipe1.competidores[i].nome)
                escolha_proximo = int(input())
                if escolha_proximo in [1, 2, 3]:
                    equipe1.competidores = equipe1.competidores[escolha_proximo-1:escolha_proximo] + equipe1.competidores[:escolha_proximo-1] + equipe1.competidores[escolha_proximo:]

if equipe1.vitorias == 10:
    print("Equipe 1 venceu o jogo!")
    vencedor = equipe1
else:
    print("Equipe 2 venceu o jogo!")
    vencedor = equipe2
    
vitorias_equipe_str = ""
for competidor in vencedor.competidores:
    vitorias_equipe_str += competidor.nome + ": " + str(competidor.vitorias) + " vitórias\n"

print(vitorias_equipe_str)

honra = max([competidor.vitorias for competidor in vencedor.competidores])
honrosa = [competidor.nome for competidor in vencedor.competidores if competidor.vitorias == honra][0]
print(f"O competidor com mais vitórias pessoais da equipe vencedora é {honrosa}.")