from playsound import playsound
import random
import threading
import os
import json
import Levenshtein
from icecream import ic

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
            try:
                globals()[commands["commands"][i]]()
            except Exception as e:
                ic(f"Error: {e}")

def break_request():
    command_react()

wake_word_reacts = ["sounds\\KVashimUslugamSir.mp3", "sounds\\ImRayaPrime.mp3"]
def wake_word_react():
    count = random.randint(0, 1)
    playsound(wake_word_reacts[count])

command_reacts = ["sounds\\WillBeRealiseSir.mp3", "sounds\\IObeySir.mp3"]
def command_react():
    count = random.randint(0, 1)
    playsound(command_reacts[count])

hello_reacts = ["sounds\\HelloSirVesglivo.mp3", "sounds\\HelloSir.mp3"]
def hello_react():
    count = random.randint(0, 1)
    playsound(hello_reacts[count])

thank_reacts = ["sounds\\AlwaysHappyToHelp.mp3", "sounds\\VsegdaKVashimUslugamSir.mp3"]
def thank_react():
    count = random.randint(0, 1)
    playsound(thank_reacts[count])

def unknown_command():
    playsound("sounds\\IdontUnderstandYouRepeatPlease.mp3")

def open_photoshop():
    os.startfile("C:\\Abobe\\Adobe Photoshop CC 2017\\Photoshop.exe")
    command_react()

def close_photoshop():
    os.system("taskkill /f /im Photoshop.exe")
    command_react()

def open_premierepro():
    os.startfile("C:\\Abobe\\Adobe Premiere Pro CC 2018\\Adobe Premiere Pro.exe")
    command_react()

def close_premierepro():
    os.system("taskkill /f /im Adobe Premiere Pro.exe")
    command_react()

def open_browser():
    os.startfile("C:\\Users\\Богдан\\AppData\\Local\\Programs\\Opera GX\\opera.exe")
    command_react()

def close_browser():
    os.system("taskkill /f /im opera.exe")
    command_react()

def open_youtube():
    os.system("start https://www.youtube.com")
    command_react()

def open_minecraft():
    os.startfile("C:\\XboxGames\\Minecraft Launcher\\Content\\Minecraft.exe") 
    command_react()

def open_telegram():
    os.startfile("C:\\Users\Богдан\\AppData\Roaming\\Telegram Desktop\\Telegram.exe")
    command_react()

def close_telegram():
    os.system("taskkill /f /im Telegram.exe")
    command_react()

def open_steam():
    os.startfile("C:\\Program Files (x86)\\Steam\\steam.exe")
    command_react()

def close_steam():
    ic("Not implemented")

def open_soundpad():
    os.startfile("C:\\MIT\\Python\\RayaPrime\\urls\\Soundpad.url")
    command_react()

def close_soundpad():
    ic("Not implemented")

def open_obs():
    os.startfile("C:\\MIT\\Python\\RayaPrime\\urls\\OBS Studio.url")
    command_react()

def close_obs():
    ic("Not implemented")

def open_drg():
    os.startfile("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Deep Rock Galactic\\FSD.exe")
    command_react()

def open_explorer_C():
    os.system("start C:\\")
    command_react()

def open_explorer_D():
    os.system("start D:\\")
    command_react() 

def open_explorer_WORKSPACE():
    os.system("start C:\\MIT")
    command_react()

def open_explorer_REVAL():
    os.system("start D:\\Реваль")
    command_react()

def open_task_manager():
    os.startfile("C:\\Windows\\System32\\Taskmgr.exe")
    command_react()