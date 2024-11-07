from machine import Pin
from time import sleep

p3 = Pin(3, Pin.IN)
p3.init(pull=Pin.PULL_UP)

while True:
    print(p3.value())
    sleep(1)
