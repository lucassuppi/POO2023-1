# Incluir bibliotecas/módulos

import os #para chamar comandos do sistema
import Exercicio
from time import sleep
import random

os.system('cls'if os.name== 'nt'else'clear')
playlist = False
playlist_musicas = []

# Funções
def Iniciar():
    print('Iniciando o programa...')
    sleep(2)

def EscolherOpcao():
    os.system('cls'if os.name== 'nt'else'clear')
    print('Mini-Spotify 🎵\n')
    print('1 - Visualizar base de dados')
    print('2 - Montar  uma  playlist')
    if playlist:
        print('3 - Visualizar a playlist')
        print('4 - Embaralhar playlist')
        print('5 - Mostrar a duração total da playlist')
    print('6 - Consultar por banda/artista')
    print('0 - Sair\n')
    resposta = input('Escolha uma opção: ')
    os.system('cls'if os.name== 'nt'else'clear')
    return resposta

def ExecutarAcao1():
    os.system('cls'if os.name== 'nt'else'clear')
    print("Visualização da base de dados\n")
    sleep(2)
    bdados = Exercicio.baseDeDados
    for i in range (len(bdados)):
        print(bdados[i])
    input('\nPressione ENTER para continuar...')

def ExecutarAcao2(): 
    global playlist, playlist_musicas
    os.system('cls'if os.name== 'nt'else'clear')
    print("Montar  uma  playlist\n")
    sleep(2)
    bdados = Exercicio.baseDeDados
    for i in range (len(bdados)):
        print(f"{i+1}. {bdados[i][0]} - {bdados[i][1]}")
    
    while True:
        try:
            escolha = int(input("Escolha o número da música para adicionar a playlist (0 para sair): "))
            if escolha == 0:
                break
            if escolha < 1 or escolha > len(bdados):
                print("Escolha inválida! Tente novamente.")
            else:
                playlist_musicas.append(bdados[escolha-1])
                print(f"{bdados[escolha-1][0]} - {bdados[escolha-1][1]} adicionada a playlist.\n")
        except ValueError:
            print("Escolha inválida! Tente novamente.")

    playlist = True

def ExecutarAcao3(): 
    os.system('cls'if os.name== 'nt'else'clear')
    if playlist:
        print("Visualizar a playlist\n")
        sleep(2)
        for i in range(len(playlist_musicas)):
            print(f'{i+1}. {playlist_musicas[i][0]} - {playlist_musicas[i][1]} - {playlist_musicas[i][4]}')
        input('Pressione enter para continuar...')

    else:
        print("Você precisa montar uma playlist primeiro!\n")
        sleep(2)

def ExecutarAcao4(): 
    os.system('cls'if os.name== 'nt'else'clear')
    if playlist:
        print("Embaralhar playlist\n")
        sleep(2)
        random.shuffle(playlist_musicas)
        for i in range(len(playlist_musicas)):
            print(f'{i+1}. {playlist_musicas[i][0]} - {playlist_musicas[i][1]} - {playlist_musicas[i][4]}')
        input('Precione enter para continuar...')

    else:
        print("Você precisa montar uma playlist primeiro!\n")
        sleep(2)

def ExecutarAcao5(): 
    os.system('cls'if os.name== 'nt'else'clear')
    if playlist:
        print("Mostrar a duração total da playlist\n")
        sleep(2)
        tempo_total = 0
        for i in range(len(playlist_musicas)):
            tempo_musica = int(playlist_musicas[i][4].split(':')[0]) * 60 + int(playlist_musicas[i][4].split(':')[1])
            tempo_total += tempo_musica
        print(f'Tempo total da playlist: {tempo_total//60}:{tempo_total%60}')
        input('\nPrecione enter para continuar...')

    else:
        print("Você precisa montar uma playlist primeiro!\n")
        sleep(2)

def ExecutarAcao6(): 
    os.system('cls'if os.name== 'nt'else'clear')
    print("Consultar por banda/artista\n")
    sleep(2)
    nome = input('Digite o nome da banda/artista: ')
    encontrada = False
    bdados = Exercicio.baseDeDados
    for i in range(len(bdados)):
        if nome.lower() == bdados[i][1].lower():
            encontrada = True
            print(f"{i+1}. {bdados[i][0]} - {bdados[i][1]} - {bdados[i][2]} - {bdados[i][3]} - {bdados[i][4]}")
    if not encontrada:
        print("Banda/artista não encontrada na base de dados.")
    input('Pressione enter para continuar...')


def Executar():
    terminarExecucao = False
    while not terminarExecucao:
        acaoUsuario = EscolherOpcao()
        if (acaoUsuario == '1'):
            ExecutarAcao1()
        elif (acaoUsuario == '2'):
            ExecutarAcao2()
        elif (acaoUsuario == '3'):
            ExecutarAcao3()
        elif (acaoUsuario == '4'):
            ExecutarAcao4()
        elif (acaoUsuario == '5'):
            ExecutarAcao5()
        elif (acaoUsuario == '6'):
            ExecutarAcao6()
        elif (acaoUsuario == '0'):
            terminarExecucao = True
        else:
            print('Escolha invalida!Tente de novo.')


def Finalizar():
    print('O programa foi encerrado!')
    # Salvar dados, encerrar processos etc

# Programa principal
if __name__ == '__main__':
    Iniciar()
    Executar()
    Finalizar()
