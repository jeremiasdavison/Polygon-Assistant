```markdown
# Polygon Assistant

Un asistente inteligente para interactuar con la blockchain de Polygon, facilitando la gestión de wallets, transacciones y la consulta de información relevante.

## ¿Por qué usarlo?

*   **Automatización:** Simplifica la interacción con la blockchain de Polygon mediante comandos intuitivos.
*   **Gestión de Wallets:** Facilita la creación, consulta y gestión de wallets de manera segura.
*   **Transacciones Simplificadas:** Permite realizar transacciones de forma rápida y eficiente.
*   **Información en Tiempo Real:** Accede a información relevante de la blockchain, como balances y movimientos.
*   **Seguridad:** Implementa medidas de seguridad para proteger tus claves privadas y transacciones.

## Tecnologías Utilizadas

*   Python
*   Web3.py
*   Librerías para el manejo de variables de entorno (`.env`)

## Instalación

1.  Clonar el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd polygonAssistant
    ```
2.  Crear un entorno virtual (recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # o venv\Scripts\activate en Windows
    ```
3.  Instalar las dependencias:
    ```bash
    pip install web3 python-dotenv
    ```
4.  Configurar las variables de entorno en el archivo `key.env`:
    *   `PRIVATE_KEY`: Tu clave privada (¡manténla segura!).
    *   `POLYGON_RPC_URL`: URL del proveedor RPC de Polygon (ej: Infura, Alchemy).

    Ejemplo de `key.env`:
    ```
    PRIVATE_KEY=0x...
    POLYGON_RPC_URL=https://polygon-rpc.com
    ```

## Uso

Ejecutar el script principal:

```bash
python main.py
```

El asistente responderá a tus comandos para interactuar con la blockchain de Polygon.  Consulta la documentación de los comandos soportados para obtener más detalles.

## Estructura del Proyecto

```
polygonAssistant/
├── assistant_actions.py    # Define las acciones del asistente (crear wallet, enviar transacciones, etc.)
├── assistant_executor.py   # Ejecuta las acciones solicitadas por el usuario.
├── interpretador.py        # Interpreta los comandos del usuario y los traduce en acciones.
├── key.env                 # Almacena las claves privadas y la URL del RPC
├── main.py                 # Punto de entrada del programa.
```

## Comentarios Destacados

*   `# 🔐 Cargar claves desde .env` (main.py):  Importante para la seguridad del proyecto, evita que las claves estén en el código.
*   `# Crear wallet`, `# Ver balance (más términos comunes)`, `# Ver movimientos (también 'transacciones' o 'transaciones')` (interpretador.py):  Indica las funcionalidades principales del asistente.
*   `# Obtener la dirección del emisor a partir de la private key`, `# Firmar y enviar` (assistant_actions.py):  Detalla el proceso de firma y envío de transacciones.

## Créditos

Desarrollado por [Tu Nombre/Organización] (opcional)

## Licencia

MIT License

## Badges

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## English Version

# Polygon Assistant

An intelligent assistant to interact with the Polygon blockchain, facilitating wallet management, transactions, and the consultation of relevant information.


## Why Use It?

*   **Automation:** Simplifies interaction with the Polygon blockchain through intuitive commands.
*   **Wallet Management:** Facilitates the creation, consultation, and management of wallets securely.
*   **Simplified Transactions:** Allows you to perform transactions quickly and efficiently.
*   **Real-Time Information:** Access relevant blockchain information, such as balances and movements.
*   **Security:** Implements security measures to protect your private keys and transactions.

## Technologies Used

*   Python
*   Web3.py
*   Libraries for environment variable handling (`.env`)

## Installation

1.  Clone the repository:
    ```bash
    git clone <REPOSITORY_URL>
    cd polygonAssistant
    ```
2.  Create a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate in Windows
    ```
3.  Install the dependencies:
    ```bash
    pip install web3 python-dotenv
    ```
4.  Configure the environment variables in the `key.env` file:
    *   `PRIVATE_KEY`: Your private key (keep it safe!).
    *   `POLYGON_RPC_URL`: Polygon RPC provider URL (e.g., Infura, Alchemy).

    `key.env` example:
    ```
    PRIVATE_KEY=0x...
    POLYGON_RPC_URL=https://polygon-rpc.com
    ```

## Usage

Run the main script:

```bash
python main.py
```

The assistant will respond to your commands to interact with the Polygon blockchain. Consult the documentation of the supported commands for more details.

## Project Structure

```
polygonAssistant/
├── assistant_actions.py    # Defines the assistant's actions (create wallet, send transactions, etc.)
├── assistant_executor.py   # Executes the actions requested by the user.
├── interpretador.py        # Interprets user commands and translates them into actions.
├── key.env                 # Stores private keys and the RPC URL (DO NOT UPLOAD THIS FILE TO GITHUB!)
├── main.py                 # Program entry point.
```

## Featured Comments

*   `# 🔐 Cargar claves desde .env` (main.py):  Important for project security, prevents keys from being in the code.
*   `# Crear wallet`, `# Ver balance (más términos comunes)`, `# Ver movimientos (también 'transacciones' o 'transaciones')` (interpretador.py):  Indicates the main features of the assistant.
*   `# Obtener la dirección del emisor a partir de la private key`, `# Firmar y enviar` (assistant_actions.py):  Details the transaction signing and sending process.

## Credits

Developed by [Your Name/Organization] (optional)

## License

MIT License

## Badges

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
```
