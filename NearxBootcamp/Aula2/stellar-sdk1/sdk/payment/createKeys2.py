from stellar_sdk import Keypair

# Gerar um par de chaves aleatório
bob_secret_key = Keypair.random()

# Exibir a chave privada
print(f"# Bob's secret Key: {bob_secret_key.secret}")

# Criar um novo objeto Keypair a partir da chave privada correta
# from_secret espera uma string, não um objeto
bob = Keypair.from_secret(bob_secret_key.secret)

# Exibir a chave pública
print(f"# Bob's public Key: {bob.public_key}")