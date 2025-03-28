import os
from dotenv import load_dotenv

from stellar_sdk import Keypair

# Carregar variáveis do arquivo .env
# não esqueça de carregar as variáveis !!!
load_dotenv()

print(f"# Alice's secret Key: {os.getenv("ALICE_SECRET_KEY")}")
print(f"# Bob's secret Key: {os.getenv("BOB_SECRET_KEY")}")