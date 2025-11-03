# Hardware & Wiring (Flex-sensor + ADS1115 + MPU6050 + I2C LCD)

## Parts (as you listed)
- Raspberry Pi 3 Model B+ (recommended)
- Glove
- Flex Sensors ×4 (or 5)
- LCD 16x2 with I2C module (PCF8574 backpack)
- ADS1115 4-channel I²C ADC (16-bit) — user listed ADS1105; use ADS1115.
- MPU6050 Accelerometer/Gyro (optional for wrist gestures)
- Jumper wires, breadboard, resistors (e.g., 10k), potentiometer (LCD contrast)
- Power supply (5V 2.5A)

## ADS1115 wiring (I2C)
- VCC -> 3.3V
- GND -> GND
- SDA -> SDA (BCM2, physical 3)
- SCL -> SCL (BCM3, physical 5)
Address is usually 0x48 (can change via ADDR pin). Find with `i2cdetect -y 1`.

## Flex sensors (voltage divider)
Each flex sensor is used in a voltage divider:
- 3.3V -> Flex sensor -> ADC input -> resistor -> GND
- Typical resistor: 47k – tune experimentally.
Connect ADC inputs to ADS1115 AIN0..AIN3 (or AIN0..AIN4 depending on ADC).

## MPU6050 wiring (I2C)
- VCC -> 3.3V
- GND -> GND
- SDA -> SDA (BCM2)
- SCL -> SCL (BCM3)

## I2C LCD (PCF8574)
- VCC -> 5V or 3.3V (check module)
- GND -> GND
- SDA -> SDA
- SCL -> SCL

