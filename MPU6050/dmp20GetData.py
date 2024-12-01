from struct import pack, unpack
from machine import SoftI2C

def getData():
    mpu.resetFIFO()
    mpu.getIntStatus()
    while mpu.getFIFOCount() != 42:
        if mpu.getFIFOCount() > 42:
            mpu.resetFIFO()
    buf = mpu.getFIFOBytes(42)
    quat = mpu.dmpGetQuaternion(buf)
    acc = mpu.dmpGetFifoAccel(buf)
    gyro = mpu.dmpGetFifoGyro(buf)
    grav = mpu.dmpGetGravity(quat)
    linac = mpu.dmpGetLinearAcc(grav, acc)
    yaw, pitch, roll = mpu.dmpGetYawPitchRoll(quat, grav)
    theta, phi, psi  = mpu.dmpGetEuler(quat)
    return yaw, pitch, roll

i2c = SoftI2C(scl=4,sda=3)

from MPU6050dmp20 import *

mpu = MPU6050dmp(i2c, '''axOff=-4387, ayOff=537, azOff=633, gxOff=128, gyOff=23, gzOff=33''')
mpu.dmpInitialize()
mpu.setDMPEnabled(True)
mpu.getIntStatus()

