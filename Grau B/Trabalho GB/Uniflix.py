# Integrantes do Grupo:
# Lucas Suppi Bernardo, Eduardo Moreira Battistello, Henrique Schuch Batalha Boeira

import csv

class Midia:
    def __init__(self, tipo, nome, ano, classificacao):
        self.tipo = tipo
        self.nome = nome
        self.ano = ano
        self.classificacao = classificacao

class Perfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.midias_favoritas = []
        self.ultimas_midias_assistidas = []

    def adicionar_midia_favorita(self, midia):
        self.midias_favoritas.append(midia)

    def remover_midia_favorita(self, midia):
        self.midias_favoritas.remove(midia)

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

def carregar_catalogo():
    catalogo = []
    with open('catalogo.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            tipo = linha[0]
            nome = linha[1]
            ano = linha[2]
            classificacao = linha[3]
            midia = Midia(tipo, nome, ano, classificacao)
            catalogo.append(midia)
    return catalogo

def carregar_usuarios():
    usuarios = []
    with open('usuarios.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            nome = linha[0]
            senha = linha[1]
            tipo_assinatura = linha[2]
            usuario = Usuario(nome, senha, tipo_assinatura)
            usuarios.append(usuario)
    return usuarios

def carregar_perfis():
    perfis = []
    with open('perfis.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            nome_usuario = linha[0]
            nome_perfil = linha[1]
            idade = linha[2]
            for usuario in usuarios:
                if usuario.nome == nome_usuario:
                    perfil = Perfil(nome_perfil, idade)
                    usuario.adicionar_perfil(perfil)
                    perfis.append(perfil)
    return perfis

def salvar_perfis():
    with open('perfis.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for usuario in usuarios:
            for perfil in usuario.perfis:
                escritor.writerow([usuario.nome, perfil.nome, perfil.idade])

def listar_midias_catalogo(catalogo):
    print("\nMídias do Catálogo:")
    for i, midia in enumerate(catalogo, start=1):
        print(f"{i}. Tipo: {midia.tipo}")
        print(f"   Nome: {midia.nome}")
        print(f"   Ano: {midia.ano}")
        print(f"   Classificação: {midia.classificacao}")
        print("--------------------")

def buscar_midia_por_titulo(titulo, catalogo):
    resultado = []
    for midia in catalogo:
        if titulo.lower() in midia.nome.lower():
            resultado.append(midia)
    return resultado

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

    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == '1':
        listar_midias_catalogo(catalogo)
        numero_midia = input("Digite o número da mídia que deseja adicionar aos favoritos: ")
        if numero_midia.isdigit():
            numero_midia = int(numero_midia)
            if 1 <= numero_midia <= len(catalogo):
                midia_selecionada = catalogo[numero_midia - 1]
                perfil.adicionar_midia_favorita(midia_selecionada)
                print(f"\nMídia {midia_selecionada.nome} adicionada aos favoritos!")
            else:
                print("Número de mídia inválido!")
        else:
            print("Número de mídia inválido!")

    elif opcao == '2':
        if len(perfil.midias_favoritas) > 0:
            print("\nMídias Favoritas:")
            for i, midia in enumerate(perfil.midias_favoritas, start=1):
                print(f"{i}. Tipo: {midia.tipo}")
                print(f"   Nome: {midia.nome}")
                print(f"   Ano: {midia.ano}")
                print(f"   Classificação: {midia.classificacao}")
                print("--------------------")
            numero_midia = input("Digite o número da mídia que deseja remover dos favoritos: ")
            if numero_midia.isdigit():
                numero_midia = int(numero_midia)
                if 1 <= numero_midia <= len(perfil.midias_favoritas):
                    midia_selecionada = perfil.midias_favoritas[numero_midia - 1]
                    perfil.remover_midia_favorita(midia_selecionada)
                    print(f"\nMídia {midia_selecionada.nome} removida dos favoritos!")
                else:
                    print("Número de mídia inválido!")
            else:
                print("Número de mídia inválido!")
        else:
            print("\nNenhuma mídia favorita encontrada!")

    elif opcao == '3':
        listar_midias_catalogo(catalogo)
        numero_midia = input("Digite o número da mídia que deseja assistir: ")
        if numero_midia.isdigit():
            numero_midia = int(numero_midia)
            if 1 <= numero_midia <= len(catalogo):
                midia_selecionada = catalogo[numero_midia - 1]
                perfil.ultimas_midias_assistidas.append(midia_selecionada)
                print(f"\nAssistindo a mídia {midia_selecionada.nome}...")
            else:
                print("Número de mídia inválido!")
        else:
            print("Número de mídia inválido!")

    elif opcao == '4':
        if len(perfil.ultimas_midias_assistidas) > 0:
            print("\nÚltimas Mídias Assistidas:")
            for i, midia in enumerate(perfil.ultimas_midias_assistidas, start=1):
                print(f"{i}. Tipo: {midia.tipo}")
                print(f"   Nome: {midia.nome}")
                print(f"   Ano: {midia.ano}")
                print(f"   Classificação: {midia.classificacao}")
                print("--------------------")
        else:
            print("\nNenhuma mídia assistida recentemente!")

    elif opcao == '5':
        titulo = input("Digite o título da mídia que deseja buscar: ")
        resultado = buscar_midia_por_titulo(titulo, catalogo)
        if len(resultado) > 0:
            print(f"\nResultados da busca por '{titulo}':")
            for i, midia in enumerate(resultado, start=1):
                print(f"{i}. Tipo: {midia.tipo}")
                print(f"   Nome: {midia.nome}")
                print(f"   Ano: {midia.ano}")
                print(f"   Classificação: {midia.classificacao}")
                print("--------------------")
        else:
            print(f"\nNenhum resultado encontrado para '{titulo}'!")

    elif opcao == '6':
        listar_midias_catalogo(catalogo)

    elif opcao == '7':
        menu_usuario(usuario)

    else:
        print("\nOpção inválida!")

    menu_perfil(usuario, perfil, catalogo)

def menu_usuario(usuario):
    print(f"\n=== Menu do Usuário: {usuario.nome} ===")
    print("Selecione uma opção:")
    print("1. Acessar Perfil")
    print("2. Adicionar Perfil")
    print("3. Remover Perfil")
    print("4. Alterar Senha")
    print("5. Alterar Plano")
    print("6. Visualizar Perfis")
    print("7. Logout")

    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == '1':
        if len(usuario.perfis) > 0:
            print("\nPerfis Disponíveis:")
            for i, perfil in enumerate(usuario.perfis, start=1):
                print(f"{i}. {perfil.nome}")
            numero_perfil = input("Digite o número do perfil que deseja acessar: ")
            if numero_perfil.isdigit():
                numero_perfil = int(numero_perfil)
                if 1 <= numero_perfil <= len(usuario.perfis):
                    perfil_selecionado = usuario.perfis[numero_perfil - 1]
                    menu_perfil(usuario, perfil_selecionado, catalogo)
                else:
                    print("Número de perfil inválido!")
            else:
                print("Número de perfil inválido!")
        else:
            print("\nNenhum perfil disponível!")

    elif opcao == '2':
        nome_perfil = input("Digite o nome do novo perfil: ")
        idade = input("Digite a idade do perfil: ")
        perfil = Perfil(nome_perfil, idade)
        usuario.adicionar_perfil(perfil)
        print(f"\nPerfil {perfil.nome} adicionado!")

    elif opcao == '3':
        if len(usuario.perfis) > 0:
            print("\nPerfis Disponíveis:")
            for i, perfil in enumerate(usuario.perfis, start=1):
                print(f"{i}. {perfil.nome}")
            numero_perfil = input("Digite o número do perfil que deseja remover: ")
            if numero_perfil.isdigit():
                numero_perfil = int(numero_perfil)
                if 1 <= numero_perfil <= len(usuario.perfis):
                    perfil_selecionado = usuario.perfis[numero_perfil - 1]
                    usuario.remover_perfil(perfil_selecionado)
                    print(f"\nPerfil {perfil_selecionado.nome} removido!")
                else:
                    print("Número de perfil inválido!")
            else:
                print("Número de perfil inválido!")
        else:
            print("\nNenhum perfil disponível!")

    elif opcao == '4':
        nova_senha = input("Digite a nova senha: ")
        usuario.senha = nova_senha
        print("\nSenha alterada com sucesso!")

    elif opcao == '5':
        novo_plano = input("Digite o novo plano (Simples/Premium): ")
        usuario.tipo_assinatura = novo_plano
        print("\nPlano alterado com sucesso!")

    elif opcao == '6':
        if len(usuario.perfis) > 0:
            print("\nPerfis Disponíveis:")
            for i, perfil in enumerate(usuario.perfis, start=1):
                print(f"{i}. {perfil.nome}")
        else:
            print("\nNenhum perfil disponível!")

    elif opcao == '7':
        print("\nLogout realizado com sucesso!")
        menu_principal()

    else:
        print("\nOpção inválida!")

    menu_usuario(usuario)

def menu_principal():
    print("=== Bem-vindo ao Meu Streaming ===")
    print("Selecione uma opção:")
    print("1. Criar Usuário")
    print("2. Fazer Login")
    print("3. Sair")

    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == '1':
        nome_usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        tipo_assinatura = input("Digite o tipo de assinatura (Simples/Premium): ")
        usuario = Usuario(nome_usuario, senha, tipo_assinatura)
        usuarios.append(usuario)
        print("\nUsuário criado com sucesso!")

    elif opcao == '2':
        nome_usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.nome == nome_usuario and usuario.senha == senha:
                usuario_encontrado = usuario
                break
        if usuario_encontrado:
            menu_usuario(usuario_encontrado)
        else:
            print("\nNome de usuário ou senha incorretos!")

    elif opcao == '3':
        print("\nSaindo...")
        salvar_perfis()
        exit()

    else:
        print("\nOpção inválida!")

    menu_principal()

catalogo = carregar_catalogo()
usuarios = carregar_usuarios()
perfis = carregar_perfis()

menu_principal()
