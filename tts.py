# src/tts.py
import subprocess

def speak_espeak(text):
    try:
        subprocess.Popen(['espeak', text])
    except Exception as e:
        print("espeak error:", e)

def speak(text):
    # lightweight: try espeak. Make sure 'espeak' is installed: sudo apt-get install espeak
    try:
        speak_espeak(text)
    except Exception as e:
        print("TTS failed:", e)
