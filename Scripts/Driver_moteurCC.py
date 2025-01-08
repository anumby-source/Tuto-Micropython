from machine import Pin, PWM

class moteurCC:

    def __init__(self, pin1=0, pin2=1, en=2, freq=1000):
        self.ina = Pin(pin1, Pin.OUT)
        self.inb = Pin(pin2, Pin.OUT)
        self.en  = PWM(en, freq=1000, duty=0)

    def avant(self, vit):   # vit=duty, entre 0 et 1023
        self.ina.on()
        self.inb.off()
        self.en.duty(vit)

    def arriere(self, vit): # vit=duty, entre 0 et 1023
        self.ina.off()
        self.inb.on()
        self.en.duty(vit)

    def stop(self):
        self.en.duty(0)
