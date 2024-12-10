from machine import Pin, Timer

def blink(t):            # t=numéro de timer
    val = led.value()
    led.value(not val)

led = Pin(8, Pin.OUT)
tim = Timer(0, period=500, callback=blink)

# pour changer la période
tim.deinit()
tim = Timer(0, period=100, callback=blink)