from machine import Pin
from time import sleep_ms

led = Pin(4, Pin.OUT)

for k in range(10):
    led.on()
    sleep_ms(500)
    led.off()
    sleep_ms(500)