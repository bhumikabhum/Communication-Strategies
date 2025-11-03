
---

## `src/lcd_i2c.py` (I2C 16x2 LCD helper)
```python
# src/lcd_i2c.py
from smbus2 import SMBus
import time

# Basic 4-bit I2C LCD driver for many PCF8574 backpacks.
class I2CLcd:
    def __init__(self, i2c_bus=1, addr=0x27, width=16):
        self.bus = SMBus(i2c_bus)
        self.addr = addr
        self.width = width
        self._init_lcd()

    def _write(self, data):
        self.bus.write_byte(self.addr, data)

    def _pulse(self, data):
        self._write(data | 0x04)
        time.sleep(0.0005)
        self._write(data & ~0x04)
        time.sleep(0.0001)

    def _write4(self, data):
        self._write(data)
        self._pulse(data)

    def _send(self, value, mode=0):
        high = value & 0xF0
        low = (value << 4) & 0xF0
        self._write4(high | mode)
        self._write4(low | mode)

    def _init_lcd(self):
        time.sleep(0.05)
        self._write4(0x30)
        time.sleep(0.0045)
        self._write4(0x30)
        time.sleep(0.00015)
        self._write4(0x30)
        time.sleep(0.00015)
        self._write4(0x20)  # 4-bit mode
        self._send(0x28)    # function set
        self._send(0x0C)    # display on, no cursor
        self._send(0x06)    # entry mode
        self.clear()

    def clear(self):
        self._send(0x01)
        time.sleep(0.002)

    def write_line(self, text, line=0):
        addr = 0x80 if line == 0 else 0xC0
        self._send(addr)
        text = text.ljust(self.width)[:self.width]
        for ch in text:
            self._send(ord(ch), mode=0x01)  # RS=1
