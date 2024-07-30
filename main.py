import recognizer
import _commands
import GUI
import ChatGPT_requests

import json
import random
import os
import pyautogui
import time
from icecream import ic

import threading

ChatGPT = ChatGPT_requests.ChatGPT(PERSONAL_ACCESS_TOKEN = "pat_bype5W9TbbG4umD60PcxLSuW9mAVaApZK1DIIqp0kVymWLLBJ7dImaz5rTTVRTrF",
                                   BOT_ID = "7377301694381801478",
                                   USER_ID = "7355571474067062789",
                                   API_URL = "https://api.coze.com/open_api/v2/chat")


Recognizer = recognizer.Recognizer("voskModels\\vosk-model-small-ru-0.4")
Recognizer.start_stream()

def wake_word_recognize():
    for text in Recognizer.recognize():
        ic(text)
        text = text.split(" ")
        if "рая" in text or "рай" in text:
            main_recognize()

def main_recognize():
    _commands.wake_word_react()   
    for text in Recognizer.recognize():
        if ("замолчи" not in text) and ("заткнись" not in text) and ("прервать запрос" not in text) and ("прервать" not in text):
            command = _commands.check_command(text)
            if command is not None:
                ic(command)
                _commands.do_command(command)
            else:
                ic(text)
                answer = ChatGPT.send_request(text)
                ic(f"GPT answer: {answer}")
                Recognizer.speaker_say(str(answer))
        else:
            ic(text)
            _commands.break_request()
            break
    

wake_word_recognize()