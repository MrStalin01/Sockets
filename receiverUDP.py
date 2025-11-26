import socket as sk
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.bind(("127.0.0.1", 23000))

print("Este recibidor esta escuchando en el puerto 23000")

while True:
    datos, direccion = sock.recvfrom(1024)
    print(f"De la direccion {direccion} llega la siguiente información:\ {datos.decode()}")