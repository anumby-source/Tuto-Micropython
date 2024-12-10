from time import localtime, sleep
from esp32 import mcu_temperature

fd = open('temperature.txt', 'w')

for k in range(10):
    fd.write(str(localtime()))
    fd.write('   température:')
    fd.write(str(mcu_temperature()))
    fd.write(' degré\r\n')
    sleep(1)

fd.close()