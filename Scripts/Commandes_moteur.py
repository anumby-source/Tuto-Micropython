from machine import Pin, PWM

ina = Pin(0, Pin.OUT)
inb = Pin(1, Pin.OUT)
en  = PWM(2, freq=1000, duty=0)

def avance(vit):
    ina.on()
    inb.off()
    en.duty(vit)

def recule(vit):
    ina.off()
    inb.on()
    en.duty(vit)

def stop():
    en.duty(0)

def vitesse():
    return en.duty()