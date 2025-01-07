import network
import socket
from time import sleep_ms

# connexion au wifi serveur
reseau = 'ESP32 Gilles'   # remplacer par le nom du réseau
mdp    = ''      # remplacer par le mot passe

sta = network.WLAN(network.STA_IF)
sta.active(True)

sta.connect(reseau, mdp)       # demande de connection
while not sta.isconnected():   # boucle d'attente
    sleep_ms(100)

addrIP = sta.ifconfig()[0]

print("connexion à " + reseau + " établie")
print("adresse IP : " + addrIP)

# préparation connection TCP
IPserv = '192.168.4.1'
port   = 1024  # n° de port [1024;65535]

clt = socket.socket()       # création du socket de connection
clt.connect((IPserv, port)) # connection au serveur
print("connection TCP établie")
