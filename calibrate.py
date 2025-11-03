# src/calibrate.py
from adc_ads1115 import ADS1115
import time

def main():
    adc = ADS1115()
    print("Reading ADS1115 channels (press Ctrl+C to stop)")
    try:
        while True:
            vals = [adc.read_channel(i) for i in range(4)]
            print(vals)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting")

if __name__ == "__main__":
    main()
