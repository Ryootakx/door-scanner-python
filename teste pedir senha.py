import getpass

escolha = input("deseja ver a senha? (s/n): ")
print("Você digitou (entre colchetes):", "[" + escolha + "]")
print("Resultado do .lower() (entre colchetes):", "[" + escolha.lower() + "]")
print("Comparação escolha.lower() == 's':", escolha.lower() == "s")

if escolha.lower() == "s":
    print(">>> ENTROU NO IF - vai mostrar senha")
    senha = input("digite sua senha: ")
else:
    print(">>> ENTROU NO ELSE - vai esconder senha")
    senha = getpass.getpass("digite sua senha: ")

print("Senha capturada:", senha)
