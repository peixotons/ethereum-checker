import random
from web3 import Web3, HTTPProvider

# Conecte-se a um provedor Ethereum, como Infura
provider_url = 'https://mainnet.infura.io/v3/ucantknow'
w3 = Web3(HTTPProvider(provider_url))

# Configuração
num_chaves = 100000

# Função para gerar uma chave privada aleatória e verificar o saldo
def verificar_chave_aleatoria(counter):
    # Gere uma chave privada aleatória
    priv_key = random.randint(1, 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)
    # Converta a chave privada em uma string hexadecimal e adicione zeros à esquerda, se necessário
    priv_key_hex = f"0x{priv_key:064x}"
    # Obtenha a chave pública e o endereço associado à chave privada
    pub_key = w3.eth.account.from_key(priv_key_hex).address

    # Verifique o saldo e o número de transações
    try:
        balance = w3.eth.get_balance(pub_key)
        tx_count = w3.eth.get_transaction_count(pub_key)

        print(f"{counter}: Endereço: {pub_key} - Saldo: {w3.from_wei(balance, 'ether')} ether - Transações: {tx_count}")
        if tx_count > 0:
            print(f"Chave privada: {priv_key_hex}")
    except Exception as e:
        print(f"Erro ao verificar o endereço {pub_key}: {e}")

# Testar várias chaves privadas aleatórias
for i in range(num_chaves):
    verificar_chave_aleatoria(i+1)
