class UnidadeMilitar:
    def mover(self):
        pass

    def atacar(self):
        pass


class Soldado(UnidadeMilitar):
    def mover(self):
        print("Soldado - Ataquei com a espada")
    
    def atacar(self):
        print("Soldado - Estou me movendo correndo")


class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("Arqueiro - Ataquei com o arco")
    
    def atacar(self):
        print("Arqueiro - Estou me movendo silenciosamente")


class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("Cavaleiro - Ataquei com o machado")
    
    def atacar(self):
        print("Cavaleiro - Estou me movendo a cavalo")


unidades = [Soldado(), Arqueiro(), Cavaleiro()]

print('Batalha Medieval')
print('🏰 · ⚔️ · 🛡️ · ⚜ · 👑 · 🗡️ · 🏹 · 🕯️\n')
for unidade in unidades:
    unidade.mover()
    unidade.atacar()
    print('')
