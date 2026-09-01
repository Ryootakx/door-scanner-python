import hashlib
senha = input("digite sua senha: ")
hash_senha = hashlib.sha256(senha.encode()).hexdigest()
print("hash gerado:", hash_senha)