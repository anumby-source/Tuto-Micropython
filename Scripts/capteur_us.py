from machine import Pin
from time import sleep_us, ticks_us

trig = Pin(3, Pin.OUT)
trig.off()
echo = Pin(4, Pin.IN, pull=Pin.PULL_DOWN)
cson = 0.347   # vitesse du son en mm/us
tmax = 1000    # temps echo max après trigger

def mesure():
    trig.on()
    sleep_us(10)
    trig.off()
    while not echo.value():
        pass
    start = ticks_us()
    while echo.value():
        pass
    tus = ticks_us() - start
    dmm = cson * tus /2
    return dmm