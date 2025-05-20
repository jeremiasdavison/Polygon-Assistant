from interpretador import interpretar_mensaje
from assistant_actions import enviar_matic, obtener_saldos_matic, listar_transacciones, crear_wallet


def assistant_executor(mensaje_usuario, private_key=None, wallet_address=None):
    comando = interpretar_mensaje(mensaje_usuario)

    match comando["accion"]:
        case "enviar_matic":
            if not private_key:
                return "⚠️ Falta la clave privada para enviar MATIC."
            resultado = enviar_matic(private_key, **comando["params"])
            return (
                f"✅ Transacción enviada:\n"
                f"🔗 Tx: {resultado['tx_hash']}\n"
                f"📤 De: {resultado['from']}\n"
                f"📥 A: {resultado['to']}\n"
                f"💸 Monto: {resultado['amount']} MATIC en {resultado['red']}"
            )

        case "crear_wallet":
            return crear_wallet()

        case "obtener_balance":
            if not wallet_address or not isinstance(wallet_address, str) or not wallet_address.startswith("0x"):
                return "⚠️ No tengo una dirección de wallet válida para consultar el balance."
            saldos = obtener_saldos_matic(wallet_address)
            red = "Polygon Mainnet" if comando["params"]["red"] == "mainnet" else "Amoy Testnet"
            return f"📊 Tu balance en {red} es: {saldos.get(red)} MATIC"

        case "listar_transacciones":
            if not wallet_address or not isinstance(wallet_address, str) or not wallet_address.startswith("0x"):
                return "⚠️ Necesito tu dirección para revisar las transacciones."
            return listar_transacciones(wallet_address, comando["params"]["red"])

        case _:
            return "🤖 No entendí tu pedido. ¿Podés reformularlo?"
