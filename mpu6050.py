# src/mpu6050.py
# Simple wrapper using mpu6050-raspberrypi library if installed.
try:
    from mpu6050 import mpu6050
except Exception:
    mpu6050 = None

class MPU:
    def __init__(self, addr=0x68):
        if mpu6050 is None:
            raise RuntimeError("mpu6050 library not installed")
        self.sensor = mpu6050(addr)

    def get_accel(self):
        return self.sensor.get_accel_data()  # returns dict x,y,z

    def get_gyro(self):
        return self.sensor.get_gyro_data()
