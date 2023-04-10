class Pais:
    def __init__(self, iso, nome, pop, dimensao, fronteira):
        self._iso = iso
        self._nome = nome
        self._populacao = pop
        self._dimensao = dimensao
        self._fronteira = fronteira

    @property
    def codigo_iso(self):
        return self._iso

    @codigo_iso.setter
    def codigo_iso(self, novo_codigo_iso):
        self._iso = novo_codigo_iso

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def populacao(self):
        return self._populacao

    @populacao.setter
    def populacao(self, nova_populacao):
        self._populacao = nova_populacao

    @property
    def dimensao(self):
        return self._dimensao

    @dimensao.setter
    def dimensao(self, nova_dimensao):
        self._dimensao = nova_dimensao

    @property
    def fronteira(self):
        return self._fronteira

    @fronteira.setter
    def fronteira(self, nova_fronteira):
        self._fronteira = nova_fronteira

    def __eq__(self, other):
        if isinstance(other, Pais):
            return self._iso == other.codigo_iso
        return False

    def eh_limitrofe(self, outro_pais):
        if isinstance(outro_pais, Pais):
            return set(self._fronteira) & set(outro_pais.fronteira)
        return False

    def densidade_populacional(self):
        return self._populacao / self._dimensao

    def vizinhos_comuns(self, outro_pais):
        if isinstance(outro_pais, Pais):
            return list(set(self._fronteira) & set(outro_pais.fronteira))
        return []

class Continente:
    def __init__(self, nome):
        self.nome = nome
        self.paises = []

    def adicionar_pais(self, pais):
        self.paises.append(pais)

    def dimensao_total(self):
        return sum([pais.dimensao for pais in self.paises])

    def populacao_total(self):
        return sum([pais.populacao for pais in self.paises])

    def densidade_populacional(self):
        return self.populacao_total() / self.dimensao_total()

    def maior_populacao(self):
        return max(self.paises, key=lambda x: x.populacao)

    def menor_populacao(self):
        return min(self.paises, key=lambda x: x.populacao)

    def maior_dimensao(self):
        return max(self.paises, key=lambda x: x.dimensao)
    
    def menor_dimensao(self):
        return min(self.paises, key=lambda x: x.dimensao)

    def razao_territorial(self):
        maior_dimensao = self.maior_dimensao().dimensao
        menor_dimensao = self.menor_dimensao().dimensao
        return maior_dimensao / menor_dimensao if menor_dimensao != 0 else 0

brasil = Pais('BR', 'Brasil', 213000000, 8515767, ['AR', 'BO', 'CO', 'GF', 'GY', 'PY', 'PE', 'SR', 'UY', 'VE'])
argentina = Pais('AR', 'Argentina', 44940000, 2780400, ['BO', 'BR', 'CL', 'PY', 'UY'])
chile = Pais('CL', 'Chile', 19460000, 756950, ['AR', 'BO', 'PE'])
bolivia = Pais('BO', 'Bolívia', 11400000, 1098581, ['AR', 'BR', 'CL', 'PY', 'PE'])

# Testando a igualdade semântica
print(brasil == argentina)  
print(argentina == chile)   
print(bolivia == argentina) 

# Testando se um país é limitrofe de outro
print(brasil.eh_limitrofe(argentina))  
print(brasil.eh_limitrofe(chile))      
print(bolivia.eh_limitrofe(chile))     

# Testando o cálculo da densidade populacional
print(brasil.densidade_populacional())  
print(argentina.densidade_populacional())  

# Testando a lista de vizinhos comuns
print(brasil.vizinhos_comuns(argentina))  
print(brasil.vizinhos_comuns(chile))      
print(bolivia.vizinhos_comuns(argentina)) 

america_do_sul = Continente('América do Sul')
america_do_sul.adicionar_pais(brasil)
america_do_sul.adicionar_pais(argentina)
america_do_sul.adicionar_pais(chile)
america_do_sul.adicionar_pais(bolivia)

print(america_do_sul.dimensao_total()) 
print(america_do_sul.populacao_total()) 
print(america_do_sul.densidade_populacional()) 
print(america_do_sul.maior_populacao().nome) 
print(america_do_sul.menor_populacao().nome) 
print(america_do_sul.maior_dimensao().nome) 
print(america_do_sul.menor_dimensao().nome) 
print(america_do_sul.razao_territorial())