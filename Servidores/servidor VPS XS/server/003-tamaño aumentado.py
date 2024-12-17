import asyncio                                                                  # Importo la librería de peticiones asincronas
import websockets                                                               # Importo la librería de sockets pero web
import ssl                                                                      # Importo la librería de conexión segura
import json                                                                     # Importo la librería de JSON

connected_clients = set()                                                       # Creo un conjunto vacio de clientes

async def handle_client(websocket, path):
    connected_clients.add(websocket) 

    try:
        async for message in websocket:
            for client in list(connected_clients):  # Crea una copia de connected_clients
                if client != websocket:
                    await client.send(message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connected_clients.remove(websocket)                               # Quita el cliente que se ha desconectado de la cola

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)                           # Estoy obligado a usar SSL en la conexión de websockets                   
ssl_context.load_cert_chain(
    "www.jotauve.es_ssl_certificate.cer",
    "www.jotauve.es_private_key.key"
    )                                                                           # Le introduzco los certificados de protocolo seguro

start_server = websockets.serve(
    handle_client,
    "jotauve.es",
    3000,
    ssl=ssl_context,
    max_size=10 * 1024 * 1024  # Ajusta el tamaño máximo a 10 MB.
)
                                                                      # Arranco el servidor

asyncio.get_event_loop().run_until_complete(start_server)                       # Arranco el asíncrono
asyncio.get_event_loop().run_forever()                                          # Ejecuto en bucle para siempre
