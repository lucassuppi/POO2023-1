import csv

class Usuario:
    def __init__(self, nome=None, sobrenome=None, data_nascimento=None, cpf=None, nome_usuario=None, senha=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.assinaturas = []

    def adicionar_assinatura(self, assinatura):
        self.assinaturas.append(assinatura)

    def cancelar_assinatura(self, id_assinatura):
        if id_assinatura < len(self.assinaturas):
            del self.assinaturas[id_assinatura]

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Sobrenome:", self.sobrenome)
        print("Data de Nascimento:", self.data_nascimento)
        print("CPF:", self.cpf)
        print("Nome de Usuário:", self.nome_usuario)
        print("Senha:", self.senha)

    def serializar(self):
        return f"{self.nome},{self.sobrenome},{self.data_nascimento},{self.cpf},{self.nome_usuario},{self.senha}"

    @staticmethod
    def desserializar(dados):
        nome, sobrenome, data_nascimento, cpf, nome_usuario, senha = dados
        return Usuario(nome, sobrenome, data_nascimento, cpf, nome_usuario, senha)


class Assinatura:
    def __init__(self, cpf=None, tipo=None, status=None):
        self.cpf = cpf
        self.tipo = tipo
        self.status = status

    def exibir_dados(self):
        print("Tipo:", self.tipo)
        print("Status:", self.status)

    def serializar(self):
        return f"{self.cpf},{self.tipo},{self.status}"

    @staticmethod
    def desserializar(dados):
        cpf, tipo, status = dados
        return Assinatura(cpf, tipo, status)


def ler_usuarios_csv(arquivo):
    usuarios = []
    with open(arquivo, newline='') as arqCSV:
        leitor = csv.reader(arqCSV, delimiter=',')
        for linha in leitor:
            if len(linha) == 6:
                usuario = Usuario.desserializar(linha)
                usuarios.append(usuario)
    return usuarios


def ler_assinaturas_csv(arquivo):
    assinaturas = []
    with open(arquivo, newline='') as arqCSV:
        leitor = csv.reader(arqCSV, delimiter=',')
        for linha in leitor:
            if len(linha) == 3:
                assinatura = Assinatura.desserializar(linha)
                assinaturas.append(assinatura)
    return assinaturas


def salvar_dados_usuarios(arquivo, usuarios):
    with open(arquivo, 'w', newline='') as arqCSV:
        escritor = csv.writer(arqCSV, delimiter=',')
        for usuario in usuarios:
            dados = usuario.serializar().split(',')
            escritor.writerow(dados)


def salvar_dados_assinaturas(arquivo, assinaturas):
    with open(arquivo, 'w', newline='') as arqCSV:
        escritor = csv.writer(arqCSV, delimiter=',')
        for assinatura in assinaturas:
            dados = assinatura.serializar().split(',')
            escritor.writerow(dados)


def exibir_menu():
    print("---- MENU ----")
    print("0 - Sair")
    print("1 - Adicionar Usuário")
    print("2 - Adicionar Assinatura")
    print("3 - Cancelar Assinatura")
    print("4 - Exibir Dados do Usuário")
    print("5 - Exibir Assinaturas do Usuário")
    print("6 - Salvar Dados")


def adicionar_usuario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    cpf = input("CPF: ")
    nome_usuario = input("Nome de Usuário: ")
    senha = input("Senha: ")

    usuario = Usuario(nome, sobrenome, data_nascimento, cpf, nome_usuario, senha)
    usuarios.append(usuario)
    print("Usuário adicionado com sucesso.")


def adicionar_assinatura():
    cpf = input("CPF do Usuário: ")
    tipo = input("Tipo de Assinatura (1 - Simples, 2 - Premium): ")
    status = "Ativa"

    if tipo == "1":
        tipo = "Simples"
    elif tipo == "2":
        tipo = "Premium"
    else:
        print("Tipo de assinatura inválido.")
        return

    assinatura = Assinatura(cpf, tipo, status)
    assinaturas.append(assinatura)
    print("Assinatura adicionada com sucesso.")


def cancelar_assinatura():
    cpf = input("CPF do Usuário: ")
    usuario_encontrado = False

    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = True
            if len(usuario.assinaturas) == 0:
                print("O usuário não possui assinaturas.")
            else:
                print("Assinaturas do Usuário:")
                for i, assinatura in enumerate(usuario.assinaturas):
                    print(i, "-", assinatura.tipo)
                id_assinatura = int(input("Digite o ID da assinatura a ser cancelada: "))
                usuario.cancelar_assinatura(id_assinatura)
                print("Assinatura cancelada com sucesso.")
            break

    if not usuario_encontrado:
        print("Usuário não encontrado.")


def exibir_dados_usuario():
    cpf = input("CPF do Usuário: ")
    usuario_encontrado = False

    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = True
            usuario.exibir_dados()
            break

    if not usuario_encontrado:
        print("Usuário não encontrado.")


def exibir_assinaturas_usuario():
    cpf = input("CPF do Usuário: ")
    usuario_encontrado = False

    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = True
            if len(usuario.assinaturas) == 0:
                print("O usuário não possui assinaturas.")
            else:
                print("--- Assinaturas do Usuário ---")
                for assinatura in usuario.assinaturas:
                    assinatura.exibir_dados()
            break

    if not usuario_encontrado:
        print("Usuário não encontrado.")


def salvar_dados():
    salvar_dados_usuarios('C:\\Users\\uKyrius\\Documents\\Projetos\\Lista 7\\arqs\\usuarios.csv', usuarios)
    salvar_dados_assinaturas('C:\\Users\\uKyrius\\Documents\\Projetos\\Lista 7\\arqs\\assinaturas.csv', assinaturas)
    print("Dados salvos com sucesso.")


usuarios = ler_usuarios_csv('C:\\Users\\uKyrius\\Documents\\Projetos\\Lista 7\\arqs\\usuarios.csv')
assinaturas = ler_assinaturas_csv('C:\\Users\\uKyrius\\Documents\\Projetos\\Lista 7\\arqs\\assinaturas.csv')

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        adicionar_usuario()
    elif opcao == "2":
        adicionar_assinatura()
    elif opcao == "3":
        cancelar_assinatura()
    elif opcao == "4":
        exibir_dados_usuario()
    elif opcao == "5":
        exibir_assinaturas_usuario()
    elif opcao == "6":
        salvar_dados()
    else:
        print("Opção inválida. Tente novamente.")
