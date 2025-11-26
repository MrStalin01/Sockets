import socket as sk
import json
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.bind(("127.0.0.1", 21000))

print("Este recibidor esta recibiendo del puerto 21000. ")

Array = []
while True:
    datos, direccion = sock.recvfrom(1024)
    mensajeDescodificado = datos.decode()

    Array.append([mensajeDescodificado, direccion])

    Respuesta = {
        "Numero mensajes: ": len(Array),
        "Ultimo mensaje: ": mensajeDescodificado
    }
    respuestaJSON = json.dumps(Respuesta)
    respuestaBytes = respuestaJSON.encode()

    sock.sendto(respuestaBytes, direccion)
    print(Array)