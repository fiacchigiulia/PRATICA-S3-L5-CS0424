import socket as so
import random

IP_ADDR= input("Inserisci l'indirizzo IP")
N_PORT= int (input("Inserisci la porta da scansionare"))
N_pacchetti= int (input("Quanti pacchetti vuoi inviare?"))

#CREARE UN SOCKET
s = so.socket(so.AF_INET, so.SOCK_DGRAM)

#CREARE PACCHETTI CON DIMENSIONE MAX 1024
packet_size=1024
packet=random.randbytes(packet_size) #genera n di byte casuali

for x in range(N_pacchetti):
    s.sendto(packet,(IP_ADDR, N_PORT)) #UTILIZZO DI SENDTO XK SPECIFICO PER UTD
    print("Invio dei pacchetti UDP\n")
s.close()





