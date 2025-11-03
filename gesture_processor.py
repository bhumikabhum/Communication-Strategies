# src/gesture_processor.py
from flex_map import FLEX_MAP, DEFAULT_THRESHOLDS
import time

class GestureProcessor:
    def __init__(self, thresholds=None, flex_map=None):
        self.thresholds = thresholds if thresholds is not None else DEFAULT_THRESHOLDS
        self.flex_map = flex_map if flex_map is not None else FLEX_MAP
        self.last_phrase = None
        # debounce / hold counters
        self.hold_time = 0.8  # seconds to hold before accepting same phrase again
        self._last_time = 0

    def readings_to_pattern(self, readings):
        # readings: list of ints (same length as thresholds)
        return tuple(1 if readings[i] >= self.thresholds[i] else 0 for i in range(len(self.thresholds)))

    def interpret(self, readings):
        pattern = self.readings_to_pattern(readings)
        phrase = self.flex_map.get(pattern)
        now = time.time()
        accepted = None
        if phrase:
            # simple debounce: only show if changed or enough time passed
            if phrase != self.last_phrase or (now - self._last_time) > self.hold_time:
                self.last_phrase = phrase
                self._last_time = now
                accepted = phrase
        else:
            # reset last phrase so next gesture can register immediately
            self.last_phrase = None
        return accepted
