import network
from time import sleep_ms

reseau = 'ESP32 Gilles'
mdp    = ''

ap = network.WLAN(network.AP_IF)
ap.config(ssid=reseau, password=pwd)
ap.active(True)

addrIP = ap.ifconfig()[0]

print("réseau " + reseau + " actif")
print("adresse IP : " + addrIP) 