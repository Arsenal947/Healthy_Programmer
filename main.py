from time import time
from datetime import datetime
from pygame import mixer


def musicPlayer(music, stopper):
    mixer.init()
    mixer.music.load(music)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
        break


def logNow(msg):
    with open("logs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == "__main__":

    init_water = time()
    init_eyes = time()
    init_physical = time()
    waterTime = 40*60
    eyesTime = 30*60
    physicalTime = 45*60


    while True:
        if time() - init_water > waterTime:
            print("Water Drinking Time. Enter 'drank' to stop the alarm")
            musicPlayer("water.mp3", "drank")
            logNow("Drank Water at: ")
            init_water = time()

        if time() - init_eyes > eyesTime:
            print("Eye Exercise Time. Enter 'doneeye' to stop the alarm")
            musicPlayer("eye.mp3", "doneeye")
            logNow("Eye Relaxed at: ")
            init_eyes = time()

        if time() - init_physical > physicalTime:
            print("Physical Exercise Time. Enter 'donephy' to stop the alarm")
            musicPlayer("physical.mp3", "donephy")
            logNow("Physical Exercise at: ")
            init_physical = time()