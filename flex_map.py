# src/flex_map.py
"""
Map patterns to phrases.

Pattern uses four flex sensors (thumb, index, middle, ring) — use tuple of length N.
Value: 1 = bent (above threshold), 0 = straight (below threshold).

You may add more patterns/phrases here. For 4 sensors, patterns are 4-tuples.
"""

# Example mapping — change to suit your glove wiring and user preferences.
FLEX_MAP = {
    (1,0,0,0): "Hello",
    (1,1,0,0): "Thank you",
    (0,1,0,0): "Yes",
    (0,1,1,0): "No",
    (0,0,0,0): "I'm fine",
    (1,1,1,1): "Need help",
    (0,0,1,0): "Where?",
    (0,0,0,1): "Stop"
}

# Default ADC thresholds (raw ADS1115 counts). You must calibrate these values per sensor.
# ADS1115 raw full scale +/-4.096V, converted raw depends on actual voltage range; read values when straight/bent.
DEFAULT_THRESHOLDS = [1000, 1000, 1000, 1000]  # tune with calibrate.py
