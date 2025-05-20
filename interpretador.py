import re

def interpretar_mensaje(mensaje):
    # Usar re.IGNORECASE para ignorar mayúsculas/minúsculas
    match_enviar = re.search(r'enviar(?:ar|á)\s+([\d\.]+)\s+matic\s+a\s+(0x[a-f0-9]{40})', mensaje, re.IGNORECASE)
    
    if match_enviar:
        cantidad = float(match_enviar.group(1))  # grupo 1 para cantidad
        destino = match_enviar.group(2)  # grupo 2 para la dirección
        # Determinar la red (mejor usar un regex más simple)
        red = "amoy" if "testnet" in mensaje.lower() or "amoy" in mensaje.lower() else "mainnet"
        
        return {
            "accion": "enviar_matic",
            "params": {
                "to_address": destino,
                "amount_matic": cantidad,
                "red": red
            }
        }

    # Crear wallet
    if any(palabra in mensaje for palabra in ["crear wallet", "crear cuenta", "crear wallet nueva", "4"]):
        return {
            "accion": "crear_wallet",
            "params": {}
        }

    # Ver balance (más términos comunes)
    if any(palabra in mensaje for palabra in ["cuánto tengo", "ver balance", "balance", "saldo", "1"]):
        red = "amoy" if "testnet" in mensaje or "amoy" in mensaje else "mainnet"
        return {
            "accion": "obtener_balance",
            "params": { "red": red }
        }

    # Ver movimientos (también 'transacciones' o 'transaciones')
    if any(palabra in mensaje for palabra in ["movimientos", "transacciones", "transaciones", "2"]):
        red = "amoy" if "testnet" in mensaje or "amoy" in mensaje else "mainnet"
        return {
            "accion": "listar_transacciones",
            "params": { "red": red }
        }

    return { "accion": "desconocida", "mensaje": mensaje }
