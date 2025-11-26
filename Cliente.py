"""Crea un programa que simule un sistema de mensajeria en elque un cliuente envia un mensaje a un servidor.
El servidor guarda los mensajes en un array bidimensional donde cada fila corresponde a un mensaje y la columna 0
contiene el mensaje en si, mientras que la columna 1 contiene el remitente. El servidor debe devolver un diccionario
 con el numero de mensajes almacenados y el ultimo mensaje recibido.
 Requerimientos:
 Servidor: debe recibir mensajes mediante sockets UDP y almacenarlos en un array bidimensional.
 Cliente: dedbe enviar mensajes al servidor y manejar errores en caso de que el servidor no este disponible.
 Uso de excepciones: manejar errores al enviar y recibir mensajes """

import socket as sk
import time
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)


try:
    cliente = input("Introduce el mensaje que deseas enviar al servidor('salir'): ")
    sock.sendto(cliente.encode(), ("127.0.0.1", 21000))
    time.sleep(3)
    respuesta, _ = sock.recvfrom(1024)
    print(f"Mensaje del servidor: {respuesta.decode()}")
except sk.timeout:
    print("El servidor no disponible")
except Exception as e:
    print(e)