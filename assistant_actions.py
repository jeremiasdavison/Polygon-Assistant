from web3 import Web3
from dotenv import load_dotenv
import os
import requests
from eth_account import Account
import secrets

load_dotenv(os.path.abspath("key.env"))
private_key = os.getenv("private_key")

# URLs RPC por red
RPC_URLS = {
    "mainnet": "https://polygon-rpc.com",
    "amoy": "https://rpc-amoy.polygon.technology"
}

def conectar_web3(red="amoy"):
    return Web3(Web3.HTTPProvider(RPC_URLS[red]))

def enviar_matic(private_key, to_address, amount_matic, red="amoy"):
    web3 = conectar_web3(red)

    # Obtener la dirección del emisor a partir de la private key
    account = web3.eth.account.from_key(private_key)
    from_address = account.address

    # Convertir a wei
    amount_wei = web3.to_wei(amount_matic, 'ether')


    # Construir la transacción
    tx = {
        'nonce': web3.eth.get_transaction_count(from_address),
        'to': to_address,
        'value': amount_wei,
        'gas': 21000,
        'gasPrice': web3.eth.gas_price,
        'chainId': web3.eth.chain_id,
        }    


    # Firmar y enviar
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    return {
        "tx_hash": web3.to_hex(tx_hash),
        "from": from_address,
        "to": to_address,
        "amount": amount_matic,
        "red": red
    }

def obtener_saldos_matic(address):
    redes = {
        "Polygon Mainnet": "https://polygon-rpc.com",
        "Amoy Testnet": "https://rpc-amoy.polygon.technology"
    }

    saldos = {}

    for nombre_red, url_rpc in redes.items():
        try:
            web3 = Web3(Web3.HTTPProvider(url_rpc))
            if web3.is_connected():
                balance_wei = web3.eth.get_balance(address)
                balance_matic = web3.from_wei(balance_wei, 'ether')
                saldos[nombre_red] = round(balance_matic, 6)
            else:
                saldos[nombre_red] = "❌ Sin conexión"
        except Exception as e:
            saldos[nombre_red] = f"⚠️ Error: {str(e)}"

    return saldos


def crear_wallet():
    # Generar una clave privada segura
    new_private_key = secrets.token_hex(32)
    new_private_key = "0x" + new_private_key

    # Crear una cuenta desde la clave privada
    new_account = Account.from_key(new_private_key)

    # Datos de la wallet
    print("📦 Tu nueva wallet de Polygon:")
    print(f"🔑 Private Key: {new_private_key}")
    print(f"🏦 Address:     {new_account.address}")




def listar_transacciones(address, red="mainnet"):
    from dotenv import load_dotenv
    import os
    load_dotenv()
    api_key = os.getenv("POLYGONSCAN_API_KEY")

    if red == "amoy":
        base_url = "https://api-amoy.polygonscan.com/api"
    else:
        base_url = "https://api.polygonscan.com/api"

    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["status"] != "1":
            return f"⚠️ No se encontraron transacciones o hubo un error."
        txs = data["result"][:5]  # Mostrar las 5 más recientes
        resumen = [f"📤 {tx['from']} → {tx['to']} | 💸 {int(tx['value'])/10**18} MATIC" for tx in txs]
        return "\n".join(resumen)
    except Exception as e:
        return f"❌ Error al consultar Polygonscan: {str(e)}"
