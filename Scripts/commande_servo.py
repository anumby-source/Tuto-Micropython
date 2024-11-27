from machine import PWM

servo = PWM(4, freq=50, duty=80)

def angle(x):
    if (x < -90) or (x > 90):
        print('angle non valide')
        return
    duty = int((1.5 + x/90)*2**16/20)
    servo.duty_u16(duty)
