#
#  Allumer la led onboard en appuyant sur BOOT
#
from machine import Pin
from time import sleep

led = Pin(8, Pin.OUT)      # onboard led
p3 = Pin(9, Pin.IN)        # bouton BOOT
p3.init(pull=Pin.PULL_UP)

while True:
    print(p3.value())
    led.value(p3.value())
    sleep(1)