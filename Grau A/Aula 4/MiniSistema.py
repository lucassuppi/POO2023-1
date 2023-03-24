import os
os.system('cls') or None

class CadastroCliente():
    def __init__(self, nome, sobrenome, nascimento, email, CPF, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento
        self.email = email
        self.CPF = CPF
        self.senha = senha
        self.tentativas = 0

    def cadastro(self):
        print('Cadastro de cliente')
        self.nome = input('Digite seu nome: ')
        self.sobrenome = input('Digite seu sobrenome: ')
        self.nascimento = input('Digite a data do seu nascimento: ')
        self.CPF = input('Digite seu CPF: ')
        self.email = input('Digite seu email: ')
        self.senha = input('Digite sua senha: ')
        os.system('cls') or None
        print('Dados salvos com sucesso.')
    
    def consultardados(self):
        os.system('cls') or None
        confere_email = input('Digite seu email: ')
        confere_senha = input('Digite sua senha: ')
        if confere_email != self.email or confere_senha != self.senha:
            self.tentativas += 1
            if self.tentativas == 3:
                print('Número máximo de tentativas atingido.')
                input('Pressione enter para voltar.')
                return
            print(f'Dados incorretos. Tentativa {self.tentativas}/3')
            input('Pressione enter para tentar novamente.')
            self.consultardados()
        else:
            os.system('cls') or None
            print('Logado com sucesso')
            print(f'Nome: {self.nome} {self.sobrenome}\nData de nascimento: {self.nascimento}\nCPF: {self.CPF}')
            input('Pressione enter para continuar.')

opcao = 0
cliente = None
while opcao != 3:
    os.system('cls') or None
    print('Mini sistema 👾')
    print('1 - Cadastrar cliente')
    print('2 - Consultar dados')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        os.system('cls') or None
        cliente = CadastroCliente('', '', '', '', '', '')
        cliente.cadastro()
    elif opcao == 2:
        if not cliente:
            os.system('cls') or None
            print('Nenhum cliente cadastrado.')
            input('Pressione enter para continuar')
        else:
            cliente.consultardados()
    elif opcao == 3:
        print('Saindo...')
    else:
        print('Opção inválida.')
