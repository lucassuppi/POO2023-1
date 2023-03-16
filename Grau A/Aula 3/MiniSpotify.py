import os
os.system('cls'if os.name== 'nt'else'clear')

class Musica:
    def __init__(self, titulo, artista, album, duracao):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao

    def visualizarDados(self):
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"Álbum: {self.album}")
        print(f"Duração: {self.duracao}")
        print()

def inserir_musicas():
    musicas = []
    continuar = True

    while continuar:
        os.system('cls'if os.name== 'nt'else'clear')
        print("Digite os dados da música ou 'sair' para encerrar:")
        titulo = input("Título: ")
        if titulo == "sair":
            continuar = False
        else:
            artista = input("Artista: ")
            album = input("Álbum: ")
            duracao = input("Duração: ")
            musica = Musica(titulo, artista, album, duracao)
            musicas.append(musica)

    print("Músicas cadastradas:")
    for musica in musicas:
        musica.visualizarDados()

inserir_musicas()

