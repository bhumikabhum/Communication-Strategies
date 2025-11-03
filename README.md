# Communication-Strategies
# Raspberry Pi Gesture Communicator (Flex-sensor + ADS1115 + I2C LCD)

**Purpose:** Assist hearing-impaired users by translating glove/flex-sensor gestures into visible text (and optional speech) using a Raspberry Pi.

**Highlights**
- Uses flex sensors mounted on a glove to detect finger bends.
- Reads analog signals using the ADS1115 (I²C, 16-bit, 4-channel ADC).
- Optional MPU6050 for wrist-motion gestures (shake, nod).
- Displays recognized phrase on a 16×2 I²C LCD (PCF8574 backpack).
- Lightweight TTS with `espeak`.

> Note: The part listed in the original component list as **ADS1105** is commonly the ADS1115 ADC — this project uses ADS1115 (16-bit I²C ADC). :contentReference[oaicite:1]{index=1}

## Files
- `src/` — source code (main.py, ADC/MPU/LCD helpers, maps, calibration)
- `hardware.md` — wiring and part list
- `requirements.txt` — Python packages
- `examples/run.sh` — example run script

