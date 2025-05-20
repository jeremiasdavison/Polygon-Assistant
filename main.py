from assistant_executor import assistant_executor
from dotenv import load_dotenv
import os

# 🔐 Cargar claves desde .env
dotenv_path = r"C:\Users\jerem\Desktop\py\polygonAPP\polygonAssistant\key.env"
load_dotenv(dotenv_path)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

print("🤖 Bienvenido a Assistant Executor \n> ")
print("Mis funciones son:\n 1. Consultar Saldo\n 2. Listar transacciones\n 3. Enviar MATIC \n 4. Crear Wallet\n 5. Salir\n")
while True:
    mensaje = input("🗣️ ¿Qué querés que haga Assistant?\n> ")

    if mensaje.lower() in ["salir", "exit", "quit", "5"]:
        print("👋 Cerrando sesión con Assistant.")
        break

    respuesta = assistant_executor(
        mensaje_usuario=mensaje,
        private_key=PRIVATE_KEY,
        wallet_address=WALLET_ADDRESS
    )
    print(respuesta)