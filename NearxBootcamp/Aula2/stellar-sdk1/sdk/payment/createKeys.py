from stellar_sdk import Keypair

# Gerar um par de chaves aleatório
# alice_secret_key é um objeto da classe Keypair
alice_secret_key = Keypair.random()

# Exibir a chave privada
print(f"# Alice's secret Key: {alice_secret_key.secret}")

# Criar um novo objeto Keypair a partir da chave privada correta
# from_secret espera uma string, não um objeto
alice = Keypair.from_secret(alice_secret_key.secret)

# Exibir a chave pública
print(f"# Alice's public Key: {alice.public_key}")