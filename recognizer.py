import json
import random
import os
import pyautogui
import time
import threading

import pyaudio
import vosk
import picovoice
import pyttsx3
from playsound import playsound
from gtts import gTTS
from pydub import AudioSegment  

from icecream import ic


class Recognizer():
    def __init__(self, vosk_model : str):
        self.vosk_model = vosk.Model(vosk_model)
        self.main_recognizer = vosk.KaldiRecognizer(self.vosk_model, 16000) # Основной распознаватель речи

    def start_stream(self):
        p = pyaudio.PyAudio()
        self.stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
        self.stream.start_stream()

    def recognize(self):
        ic("recognizer_started")
        while True:
            data = self.stream.read(num_frames = 4000, exception_on_overflow = False)
            if (self.main_recognizer.AcceptWaveform(data)) and (len(data) > 0):
                answer = json.loads(self.main_recognizer.Result())
                if answer["text"]:
                    yield answer["text"]

class Speaker:
    def __init__(self):
        pass
    
    def get_robo_effect(self, file):
        original_audio = AudioSegment.from_file(file)

        offset = 20
        num_copies = 10
        combined_duration = len(original_audio) + 1000

        combined = AudioSegment.silent(duration = combined_duration)

        for i in range(num_copies):
            copy = original_audio - (i * 4)
            combined = combined.overlay(copy, position = i * offset)

        combined.export("sounds\\output_with_robo.mp3", format = "mp3")

    def speaker_say(self, text : str):
        tts = gTTS(text = text, lang = "ru")
        tts.save("sounds\\output.mp3")

        self.get_robo_effect("sounds\\output.mp3")

        playsound("sounds\\output_with_robo.mp3")
        os.remove("sounds\\output_with_robo.mp3")
        os.remove("sounds\\output.mp3")