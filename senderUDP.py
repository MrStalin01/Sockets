import socket as sk
import time

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

salir = False
while not salir:
    mensaje = input("Introduce el  mensaje que deseas enviar al servior (o escribe 'salir'): \n")
    sock.sendto(mensaje.encode(), ("127.0.0.1", 23000))
    print("El mensaje esta enviado")
    time.sleep(1)
    if mensaje == "salir":
        salir = True