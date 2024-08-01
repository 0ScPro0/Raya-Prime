from playsound import playsound
import random
import threading
import os
import json
import Levenshtein
import recognizer
from icecream import ic

Speaker = recognizer.Speaker()

def check_command(command):
    distances = []
    commands = json.load(open("commands.json", "rb"))
    commands = list(commands["commands"].keys())
    
    for i in range(len(commands)):
        distance_count = Levenshtein.distance(commands[i], command)
        distances.append(distance_count)

    if ((len(commands[distances.index(min(distances))]) + len(command) - min(distances)) / (len(commands[distances.index(min(distances))]) + len(command)) >= 0.6):  
            return commands[distances.index(min(distances))]
    
    else:
        return None

def do_command(command):
    commands = json.load(open("commands.json", "rb"))
    for i in commands["commands"].keys():
        if i == command:
            if commands["commands"][i] != "None":
                try:
                    globals()[commands["commands"][i]]()
                except:
                    os.system(commands["commands"][i])
                    command_react()
            else:
                Speaker.speaker_say("Данная функция сейчас не доступна, прошу прощения, сэр")

def break_request():
    command_react()

wake_word_reacts = ["К вашим услугам, сэр", "Я - Райя Прайм", "Да, сэр?"]
def wake_word_react():
    Speaker.speaker_say(random.choice(wake_word_reacts))

command_reacts = ["Будет исполнено, сэр", "Слушаюсь, сэр", "Одну минуту, сэр"]
def command_react():
    Speaker.speaker_say(random.choice(command_reacts))

hello_reacts = ["Приветствую, сэр", "Здравствуйте, сэр"]
def hello_react():
    Speaker.speaker_say(random.choice(hello_reacts))

thank_reacts = ["Всегда рада помочь вам, сэр", "Всегда к вашим услугам, сэр"]
def thank_react():
    Speaker.speaker_say(random.choice(thank_reacts))

def unknown_command():
    Speaker.speaker_say("Я не поняла ваш запрос, повторите его еще раз, пожалуйста!")
