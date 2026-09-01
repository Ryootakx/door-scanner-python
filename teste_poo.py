import hashlib
import getpass

class Usuario:
    def __init__(self, nome, senha_hash):
        self.nome = nome
        self.senha_hash = senha_hash

    def verificar_senha(self, senha_digitada):
        hash_digitado = hashlib.sha256(senha_digitada.encode()).hexdigest()
        return self.senha_hash == hash_digitado


class SistemaLogin:
    def __init__(self):
        self.usuarios = []

    def carregar_usuarios(self):
        try:
            arquivo = open("testes/usuarios.txt1", "r")
        except FileNotFoundError:
            print("Erro: o arquivo usuarios.txt1 nao foi encontrado.")
            exit()

        for linha in arquivo:
            linha = linha.strip()
            partes = linha.split(",")
            nome = partes[0]
            senha_hash = partes[1]
            usuario_novo = Usuario(nome, senha_hash)
            self.usuarios.append(usuario_novo)
        arquivo.close()

    def fazer_login(self):
        nome_digitado = input("digite seu nome de usuario: ")
        senha_digitada = getpass.getpass("digite sua senha: ")

        for u in self.usuarios:
            if u.nome == nome_digitado and u.verificar_senha(senha_digitada):
                return True

        return False

    def cadastrar_usuario(self):
        while True:
            nome_novo = input("Digite o nome de usuario que usara: ")
            nome_existe = False
            for u in self.usuarios:
                if u.nome == nome_novo:
                    nome_existe = True
            if nome_existe:
                print("Esse nome de usuario ja existe, tente outro.")
            else:
                break

        senha_nova = getpass.getpass("Digite a senha que voce usara: ")
        hash_senha = hashlib.sha256(senha_nova.encode()).hexdigest()

        arquivo = open("testes/usuarios.txt1", "a")
        arquivo.write("\n" + nome_novo + "," + hash_senha)
        arquivo.close()

        usuario_novo = Usuario(nome_novo, hash_senha)
        self.usuarios.append(usuario_novo)

        print()
        print("Usuario cadastrado com sucesso!")


sistema = SistemaLogin()
sistema.carregar_usuarios()

while True:
    print("1- fazer login.")
    print("2- cadastrar novo usuario.")
    print("3- sair.")
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        if sistema.fazer_login():
            print("Acesso permitido!")
        else:
            print("Acesso negado!")
    elif opcao == "2":
        sistema.cadastrar_usuario()
    elif opcao == "3":
        print("saindo...")
        break
    else:
        print("opcao invalida, tente novamente.")

    print()