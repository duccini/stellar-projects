import os
from dotenv import load_dotenv

from stellar_sdk import Keypair

# Carregar variáveis do arquivo .env
load_dotenv()


def create_alice_wallet():
    print("✅ # Alice's wallet created (SENDER)")
    alice_secret_key = os.getenv("ALICE_SECRET_KEY")
    alice = Keypair.from_secret(alice_secret_key)
    assert alice.public_key == "GA7ZGTZYVWZZ2EU7A7L2ABULTILSR534U3OM4SC3KKXOTXIAZ5ABTUIK"

    return alice


def create_bob_wallet():
    print("✅ # Bob's wallet created (RECEIVER)")
    bob_secret_key = os.getenv("BOB_SECRET_KEY")
    bob = Keypair.from_secret(bob_secret_key)
    assert bob.public_key == "GDTXOJDSZXSXB72MNNS2SJCPLK3SYCXWPTCPBXXNO5OSQYJMEW6A5O6Z"

    return bob





create_alice_wallet()
create_bob_wallet()