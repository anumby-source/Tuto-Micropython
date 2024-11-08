#
#  Faire clignoter une led (externe ou onboard)
#
from machine import Pin
from time import sleep_ms

led = Pin(8, Pin.OUT)  #  onbard led
# led = Pin(4, Pin.OUT)  #  led externe

for k in range(10):
    led.on()     # équivalent à led.value(1)
    sleep_ms(500)
    led.off()    # équivalent à led.value(0)
    sleep_ms(500)