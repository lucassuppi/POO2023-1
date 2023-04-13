class Pais:
    def __init__(self, codigo_iso, nome, populacao, dimensao):
        self._codigo_iso = codigo_iso
        self._nome = nome
        self._populacao = populacao
        self._dimensao = dimensao
        self._fronteiras = []

    def __eq__(self, outro_pais):
        if isinstance(outro_pais, Pais):
            return self._codigo_iso == outro_pais.get_codigo_iso()
        return False

    def get_codigo_iso(self):
        return self._codigo_iso

    def set_codigo_iso(self, codigo_iso):
        self._codigo_iso = codigo_iso

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_populacao(self):
        return self._populacao

    def set_populacao(self, populacao):
        self._populacao = populacao

    def get_dimensao(self):
        return self._dimensao

    def set_dimensao(self, dimensao):
        self._dimensao = dimensao

    def get_fronteiras(self):
        return self._fronteiras

    def set_fronteiras(self, fronteiras):
        self._fronteiras = fronteiras

    def eh_limitrofe(self, outro_pais):
        return outro_pais.get_codigo_iso() in self._fronteiras
    
    def densidade_populacional(self):
        return self._populacao / self._dimensao
    
    def vizinhos_comuns(self, outro_pais):
        if isinstance(outro_pais, Pais):
            vizinhos = list(set(self.get_fronteiras()) & set(outro_pais.get_fronteiras()))
            return vizinhos
        return []

brasil = Pais("BRA", "Brasil", 211755692, 8515767)
argentina = Pais("ARG", "Argentina", 44938712, 2780400)
uruguai = Pais("URY", "Uruguai", 3473730, 176215)
paraguai = Pais("PRY", "Paraguai", 7152703, 406752)

brasil.set_fronteiras(["ARG", "BOL", "COL", "GUF", "GUY", "PRY", "PER", "SUR", "URY", "VEN"])
argentina.set_fronteiras(["BOL", "BRA", "CHL", "PRY", "URY"])
paraguai.set_fronteiras(["ARG", "BOL", "BRA"])

print(brasil.get_codigo_iso()) 
print(brasil.get_nome()) 
print(brasil.get_populacao()) 
print(brasil.get_dimensao()) 

brasil.set_populacao(212559417)
print(brasil.get_populacao()) 

print(brasil == argentina)

print(brasil.eh_limitrofe(argentina))
print(brasil.eh_limitrofe(uruguai))
print(brasil.eh_limitrofe(paraguai))
print(argentina.eh_limitrofe(uruguai))

print(brasil.densidade_populacional())

vizinhos_em_comum = brasil.vizinhos_comuns(argentina)
print(vizinhos_em_comum)

# ------------------------------------------------------------------------ #

class Continente:
    def __init__(self, nome):
        self.nome = nome
        self.paises = []

    def adicionar_pais(self, pais):
        if pais not in self.paises:
            self.paises.append(pais)

    def dimensao_total(self):
        return sum(pais.get_dimensao() for pais in self.paises)

    def populacao_total(self):
        return sum(pais.get_populacao() for pais in self.paises)

    def densidade_populacional(self):
        return self.populacao_total() / self.dimensao_total()

    def pais_maior_populacao(self):
        return max(self.paises, key=lambda pais: pais.get_populacao())

    def pais_menor_populacao(self):
        return min(self.paises, key=lambda pais: pais.get_populacao())

    def pais_maior_dimensao(self):
        return max(self.paises, key=lambda pais: pais.get_dimensao())

    def pais_menor_dimensao(self):
        return min(self.paises, key=lambda pais: pais.get_dimensao())

    def razao_maior_menor_dimensao(self):
        pais_maior = self.pais_maior_dimensao()
        pais_menor = self.pais_menor_dimensao()
        return pais_maior.get_dimensao() / pais_menor.get_dimensao()


america_sul = Continente("América do Sul")
america_sul.adicionar_pais(brasil)
america_sul.adicionar_pais(argentina)
america_sul.adicionar_pais(uruguai)
america_sul.adicionar_pais(paraguai)

print("Dimensão total:", america_sul.dimensao_total())
print("População total:", america_sul.populacao_total())
print("Densidade populacional:", america_sul.densidade_populacional())
print("País com maior população:", america_sul.pais_maior_populacao().get_nome())
print("País com menor população:", america_sul.pais_menor_populacao().get_nome())
print("País de maior dimensão territorial:", america_sul.pais_maior_dimensao().get_nome())
print("País de menor dimensão territorial:", america_sul.pais_menor_dimensao().get_nome())
print("Razão territorial do maior e menor país:", america_sul.razao_maior_menor_dimensao())
