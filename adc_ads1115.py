# src/adc_ads1115.py
from smbus2 import SMBus
import time

# Small ADS1115 single-ended reading helper.
# Default i2c address 0x48. Uses single-shot conversion mode.
class ADS1115:
    def __init__(self, i2c_bus=1, address=0x48):
        self.bus = SMBus(i2c_bus)
        self.addr = address
        # Register addresses
        self.CONVERSION_REG = 0x00
        self.CONFIG_REG = 0x01
        # PGA and data rate defaults
        self.OS_SINGLE = 0x8000
        self.MUX = {
            0: 0x4000, 1: 0x5000, 2: 0x6000, 3: 0x7000
        }
        self.PGA_4_096V = 0x0200  # +/-4.096V
        self.MODE_SINGLE = 0x0100
        self.DATA_RATE_128SPS = 0x0080
        self.COMP = 0x0003

    def read_channel(self, channel):
        if channel not in (0,1,2,3):
            raise ValueError("ADS1115 channel must be 0..3")
        config = (self.OS_SINGLE |
                  self.MUX[channel] |
                  self.PGA_4_096V |
                  self.MODE_SINGLE |
                  self.DATA_RATE_128SPS |
                  self.COMP)
        # write config (16 bits)
        self.bus.write_i2c_block_data(self.addr, self.CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])
        # wait for conversion (depends on data rate: 1/128 s ~ 8ms)
        time.sleep(0.01)
        data = self.bus.read_i2c_block_data(self.addr, self.CONVERSION_REG, 2)
        raw = (data[0] << 8) | data[1]
        # convert twos complement
        if raw & 0x8000:
            raw -= 1 << 16
        return raw
