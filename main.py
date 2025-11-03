# src/main.py
import time
from lcd_i2c import I2CLcd
from adc_ads1115 import ADS1115
from gesture_processor import GestureProcessor
from tts import speak
try:
    from mpu6050 import mpu6050
    HAVE_MPU = True
except Exception:
    HAVE_MPU = False

def main():
    lcd = I2CLcd(i2c_bus=1, addr=0x27, width=16)  # change addr if different
    adc = ADS1115(i2c_bus=1, address=0x48)
    gp = GestureProcessor()

    # optional MPU6050 usage (wrist gestures)
    if HAVE_MPU:
        mpu = mpu6050(0x68)
    else:
        mpu = None

    lcd.clear()
    lcd.write_line("Gesture Commun.", 0)
    lcd.write_line("Ready...", 1)
    time.sleep(1.0)

    try:
        while True:
            # read 4 channels (flex sensors)
            readings = [adc.read_channel(i) for i in range(4)]
            # convert raw ADS1115 values (tend to be negative for some configs; absolute is OK for thresholding)
            readings = [abs(r) for r in readings]
            phrase = gp.interpret(readings)
            if phrase:
                print("Recognized:", phrase)
                lcd.clear()
                lcd.write_line(phrase, 0)
                # optional: second line show pattern or reading small debug
                lcd.write_line(" ".join(str(int(x)) for x in readings)[:16], 1)
                speak(phrase)
            else:
                # show hint
                lcd.write_line("Make Gesture", 0)
                lcd.write_line("", 1)
            # optional wrist-gesture detection using MPU6050
            if mpu:
                accel = mpu.get_accel_data()
                # example: sudden shake detection
                if abs(accel['x']) > 15 or abs(accel['y']) > 15:
                    lcd.clear()
                    lcd.write_line("Shake Detected", 0)
                    speak("Attention")
                    time.sleep(1.0)

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopping")
    finally:
        pass

if __name__ == "__main__":
    main()
