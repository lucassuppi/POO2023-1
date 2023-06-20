import csv

class Usuario:
    def __init__(self, nome, senha, tipo_assinatura):
        self.nome = nome
        self.senha = senha
        self.tipo_assinatura = tipo_assinatura
        self.perfis = []

    def adicionar_perfil(self, perfil):
        self.perfis.append(perfil)

    def remover_perfil(self, perfil):
        self.perfis.remove(perfil)

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha

    def alterar_plano(self, novo_plano):
        self.tipo_assinatura = novo_plano

class Perfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Midia:
    def __init__(self, tipo, nome, data_lancamento, classificacao):
        self.tipo = tipo
        self.nome = nome
        self.data_lancamento = data_lancamento
        self.classificacao = classificacao

def menu_principal():
    print("=== Bem-vindo ao Meu Streaming ===")
    print("Selecione uma opção:")
    print("1. Criar usuário")
    print("2. Fazer login")
    print("3. Sair")

def menu_usuario(usuario, catalogo):
    print(f"\n=== Menu do Usuário: {usuario.nome} ===")
    print("Selecione uma opção:")
    print("1. Acessar Perfil")
    print("2. Adicionar perfil")
    print("3. Remover perfil")
    print("4. Alterar senha")
    print("5. Alterar plano")
    print("6. Visualizar perfis disponíveis")
    print("7. Logout")

    print("\nPerfis disponíveis:")
    for perfil in usuario.perfis:
        print(perfil.nome)

def menu_perfil(usuario, perfil, catalogo):
    print(f"\n=== Menu do Perfil: {perfil.nome} ===")
    print("Selecione uma opção:")
    print("1. Adicionar mídia aos favoritos")
    print("2. Remover mídia dos favoritos")
    print("3. Assistir mídia")
    print("4. Listar últimas mídias assistidas")
    print("5. Buscar mídia por título")
    print("6. Listar mídias disponíveis")
    print("7. Voltar ao menu do usuário")

def listar_midias_catalogo(catalogo):
    print("\nMídias do Catálogo:")
    for i, midia in enumerate(catalogo, start=1):
        print(f"{i}. Tipo: {midia.tipo}")
        print(f"   Nome: {midia.nome}")
        print(f"   Data de Lançamento: {midia.data_lancamento}")
        print(f"   Classificação: {midia.classificacao}")
        print("--------------------")

def filtrar_midias_por_classificacao(perfil, catalogo):
    if int(perfil.idade) >= 18:
        return catalogo
    else:
        return [midia for midia in catalogo if midia.classificacao in ["Livre", "Abaixo de 18 anos"]]

def carregar_usuarios_csv():
    usuarios = []
    with open('usuarios.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar cabeçalho
        for row in reader:
            usuario = Usuario(row[0], row[1], row[2])
            usuarios.append(usuario)
    return usuarios

def carregar_perfis_csv(usuarios):
    perfis = []
    with open('perfis.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar cabeçalho
        for row in reader:
            perfil = Perfil(row[1], row[2])
            for usuario in usuarios:
                if usuario.nome == row[0]:
                    usuario.adicionar_perfil(perfil)
                    break
            perfis.append(perfil)
    return perfis

def carregar_catalogo_csv():
    catalogo = []
    with open('catalogo.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar cabeçalho
        for row in reader:
            midia = Midia(row[0], row[1], row[2], row[3])
            catalogo.append(midia)
    return catalogo

usuarios = carregar_usuarios_csv()
perfis = carregar_perfis_csv(usuarios)
catalogo = carregar_catalogo_csv()

def buscar_midia_por_titulo(titulo, catalogo):
    resultado = []
    for midia in catalogo:
        if titulo.lower() in midia.nome.lower():
            resultado.append(midia)
    return resultado

def menu_assistir_midia(perfil, catalogo):
    listar_midias_catalogo(catalogo)
    numero_midia = int(input("\nSelecione o número da mídia que deseja assistir: "))
    if numero_midia >= 1 and numero_midia <= len(catalogo):
        midia_selecionada = catalogo[numero_midia - 1]
        perfil.adicionar_ultima_midia_assistida(midia_selecionada)
        print(f"\nVocê está assistindo: {midia_selecionada.nome}")
    else:
        print("Número de mídia inválido!")

def menu_usuario(usuario):
    print(f"\n=== Menu do Usuário: {usuario.nome} ===")
    print("Selecione uma opção:")
    print("1. Acessar Perfil")
    print("2. Adicionar perfil")
    print("3. Remover perfil")
    print("4. Alterar senha")
    print("5. Alterar plano")
    print("6. Visualizar perfis disponíveis")
    print("7. Logout")

    print("\nPerfis disponíveis:")
    for perfil in usuario.perfis:
        print(perfil.nome)

usuarios = carregar_usuarios_csv()
perfis = carregar_perfis_csv(usuarios)
catalogo = carregar_catalogo_csv()

def buscar_midia_por_titulo(titulo, catalogo):
    resultado = []
    for midia in catalogo:
        if titulo.lower() in midia.nome.lower():
            resultado.append(midia)
    return resultado

def menu_assistir_midia(perfil, catalogo):
    listar_midias_catalogo(catalogo)
    numero_midia = int(input("\nSelecione o número da mídia que deseja assistir: "))
    if numero_midia >= 1 and numero_midia <= len(catalogo):
        midia_selecionada = catalogo[numero_midia - 1]
        perfil.adicionar_ultima_midia_assistida(midia_selecionada)
        print(f"\nVocê está assistindo: {midia_selecionada.nome}")
    else:
        print("Número de mídia inválido!")

def menu_perfil(usuario, perfil, catalogo):
    print(f"\n=== Menu do Perfil: {perfil.nome} ===")
    print("Selecione uma opção:")
    print("1. Adicionar mídia aos favoritos")
    print("2. Remover mídia dos favoritos")
    print("3. Assistir mídia")
    print("4. Listar últimas mídias assistidas")
    print("5. Buscar mídia por título")
    print("6. Listar mídias disponíveis")
    print("7. Voltar ao menu do usuário")

    while True:
        opcao = input("\nDigite o número da opção desejada: ")
        if opcao == '1':
            listar_midias_catalogo(catalogo)
            numero_midia = int(input("\nSelecione o número da mídia que deseja adicionar aos favoritos: "))
            if numero_midia >= 1 and numero_midia <= len(catalogo):
                midia_selecionada = catalogo[numero_midia - 1]
                perfil.adicionar_midia_favorita(midia_selecionada)
                print(f"\nMídia {midia_selecionada.nome} adicionada aos favoritos!")
            else:
                print("Número de mídia inválido!")

        elif opcao == '2':
            if perfil.midias_favoritas:
                print("\nMídias favoritas:")
                for i, midia in enumerate(perfil.midias_favoritas, start=1):
                    print(f"{i}. Tipo: {midia.tipo}")
                    print(f"   Nome: {midia.nome}")
                    print(f"   Data de Lançamento: {midia.data_lancamento}")
                    print(f"   Classificação: {midia.classificacao}")
                    print("--------------------")

                numero_midia = int(input("\nSelecione o número da mídia que deseja remover dos favoritos: "))
                if numero_midia >= 1 and numero_midia <= len(perfil.midias_favoritas):
                    midia_selecionada = perfil.midias_favoritas[numero_midia - 1]
                    perfil.remover_midia_favorita(midia_selecionada)
                    print(f"\nMídia {midia_selecionada.nome} removida dos favoritos!")
                else:
                    print("Número de mídia inválido!")
            else:
                print("\nNão há mídias favoritas!")

        elif opcao == '3':
            menu_assistir_midia(perfil, catalogo)

        elif opcao == '4':
            if perfil.ultimas_midias_assistidas:
                print("\nÚltimas Mídias Assistidas:")
                for i, midia in enumerate(perfil.ultimas_midias_assistidas, start=1):
                    print(f"{i}. Tipo: {midia.tipo}")
                    print(f"   Nome: {midia.nome}")
                    print(f"   Data de Lançamento: {midia.data_lancamento}")
                    print(f"   Classificação: {midia.classificacao}")
                    print("--------------------")
            else:
                print("\nNão há últimas mídias assistidas!")

        elif opcao == '5':
            titulo = input("\nDigite o título da mídia que deseja buscar: ")
            resultado = buscar_midia_por_titulo(titulo, catalogo)
            if resultado:
                print("\nResultado da busca:")
                for i, midia in enumerate(resultado, start=1):
                    print(f"{i}. Tipo: {midia.tipo}")
                    print(f"   Nome: {midia.nome}")
                    print(f"   Data de Lançamento: {midia.data_lancamento}")
                    print(f"   Classificação: {midia.classificacao}")
                    print("--------------------")
            else:
                print("\nNenhuma mídia encontrada com esse título!")

        elif opcao == '6':
            listar_midias_catalogo(catalogo)

        elif opcao == '7':
            break

        else:
            print("Opção inválida! Digite novamente.")

def menu_usuario(usuario):
    print(f"\n=== Menu do Usuário: {usuario.nome} ===")
    print("Selecione uma opção:")
    print("1. Acessar Perfil")
    print("2. Adicionar perfil")
    print("3. Remover perfil")
    print("4. Alterar senha")
    print("5. Alterar plano")
    print("6. Visualizar perfis disponíveis")
    print("7. Logout")

    print("\nPerfis disponíveis:")
    for perfil in usuario.perfis:
        print(perfil.nome)

def criar_usuario():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    tipo_assinatura = input("Digite o tipo de assinatura (simples, premium): ")
    usuario = Usuario(nome, senha, tipo_assinatura)
    usuarios.append(usuario)
    print(f"\nUsuário {nome} criado com sucesso!")

def fazer_login():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    for usuario in usuarios:
        if usuario.nome == nome and usuario.senha == senha:
            menu_usuario(usuario)
            return
    print("\nNome de usuário ou senha inválidos!")

def main():
    while True:
        menu_principal()
        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == '1':
            criar_usuario()

        elif opcao == '2':
            fazer_login()

        elif opcao == '3':
            break

        else:
            print("Opção inválida! Digite novamente.")

if __name__ == "__main__":
    main()
