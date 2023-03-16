#Definição da Classe Mago

class Mago:
    def __init__(self, nome, idade, escola, altura, magia, nhabilidade):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola
        self.altura = altura
        self.magia = magia
        self.nhabilidade = nhabilidade

    def dados(self):
        print(f'Dados do mago:\n{self.nome} - {self.idade} - {self.escola} - {self.altura} - {self.magia} - {self.nhabilidade}')
        
    def andar(self):
        print(f'{self.nome}: Estou andando')
    
    def falar(self):
        print(f'{self.nome}: Olá amigue!')
        
    def invocarMagia(self):
        print(f'{self.nome}: Invocando magia!')

    def utlizacaomagia(self):
        print(f'A magia {self.magia} foi utilizada por {self.nome}')

    def abaixar(self):
        print(f'{self.nome}: Precisei me abaixar pois tenho {self.altura} cm')

    def poder(self):
        print(f'Poder de habilidade do mago {self.nome}: {self.nhabilidade}')

        
        
#Istanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts', 170, 'Expelliarmus', 98)
gd = Mago('Gandalf', 2000, 'Magia Cinza', 190, 'Bola de fogo', 85)
ad = Mago('Alvo Dumbledore', 80, 'Hogwarts', 180, 'Estupefaça', 100)
gg = Mago('Gellert Grindewald', 38, 'Instituto Durmstrang', 175, 'Expecto Patronum', 89)
lv = Mago('Lord Voldemort', 49, 'Sonserina', 188, 'Avada Kedavra', 99)

hp.dados()
hp.andar(), hp.falar(), hp.invocarMagia(), hp.abaixar(), hp.utlizacaomagia(), hp.poder()

print()

gd.dados()
gd.andar(), gd.falar(), gd.invocarMagia, gd.abaixar(), gd.utlizacaomagia(), gd.poder()

print()

ad.dados()
ad.andar(), ad.falar(), ad.invocarMagia(), ad.abaixar(), ad.utlizacaomagia(), ad.poder()

print()

gg.dados()
gg.andar(), gg.falar(), gg.invocarMagia(), gg.abaixar(), gg.utlizacaomagia(), gg.poder()

print()

lv.dados()
lv.andar(), lv.falar(), lv.invocarMagia(), lv.abaixar(), lv.utlizacaomagia(), lv.poder()


