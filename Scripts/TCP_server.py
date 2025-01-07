import network
import socket
from time import sleep_ms

# création de l'Access Point wifi
reseau = 'ESP32 Gilles'
mdp    = ''

ap = network.WLAN(network.AP_IF)
ap.config(ssid=reseau, password=mdp)
ap.active(True)

addrIP = ap.ifconfig()[0]

print("réseau " + reseau + " actif")
print("adresse IP : " + addrIP) 

# préparation connection TCP
port   = 1024  # n° de port [1024;65535]

conn = socket.socket()    # création du socket de connection
conn.bind((addrIP, port)) # affectation socket <-> (adresse, port)
conn.listen(1)            # nb de connections entrantes simultanées

serv, addrClt = conn.accept()  # attente de connection d'un client
                               # serv    = socket de communication
                               # addrClt = adresse IP client
print("connection entrante avec l'adresse IP : ", addrClt[0])


