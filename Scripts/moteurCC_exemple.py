from Driver_moteurCC import moteurCC
from time import sleep

mg = moteurCC()   # arguments par défaut: pin1=0, pin2=1, en=2
md = moteurCC(pin1=3, pin2=4, en=5)

mg.avance(800)
sleep(2)
md.recule(1000)
sleep(2)
mg.stop()
md.stop()