#
#  Afficher la valeur de la pin 3 toutes les secondes
#
from machine import Pin
from time import sleep

p3 = Pin(3, Pin.IN)
p3.init(pull=Pin.PULL_UP)  # valeur 1 quand p3 est en l'air

while True:
    print(p3.value())  # connecter à GND pour changer la valeur
    sleep(1)
