from machine import Pin
from time import ticks_ms

def mon_handler(p):
    global t
    if ticks_ms() - t > 20:
        print("pin 3")
        t = ticks_ms()

p3 = Pin(3, Pin.IN, Pin.PULL_DOWN)
p3.irq(trigger=Pin.IRQ_RISING, handler=mon_handler)
t = ticks_ms()