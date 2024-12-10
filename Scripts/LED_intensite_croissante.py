from machine import PWM
from time import sleep_ms

led  = PWM(8, freq=1000, duty=1023)   # onbard LED

for k in range(100):
    print(led.duty()-10)
    led.duty(led.duty() - 10)
    sleep_ms(20)

led.duty(1023)