import network
from time import sleep_ms

reseau = 'mon_reseau'   # remplacer par le nom du réseau
mdp    = 'mon_mdp'      # remplacer par le mot passe

sta = network.WLAN(network.STA_IF)
sta.active(True)

sta.connect(reseau, mdp)       # demande de connection
while not sta.isconnected():   # boucle d'attente
    sleep_ms(100)

addrIP = sta.ifconfig()[0]

print("connexion à " + reseau + " établie")
print("adresse IP : " + addrIP)