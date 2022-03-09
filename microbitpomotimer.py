from microbit import *
import speech
import music
import audio

pomo_cycle = 1
time = 0
display.show(Image.PACMAN)

def timer_25():
    speech.say("Ready player 1!", speed=82, pitch=72, throat=110, mouth=105)
    music.play(music.POWER_UP)
    global pomo_cycle
    time = 25 * 60
    while time > 0:
        time -= 1
        #this animation should generate roughly one second of delay
        display.show(Image.ALL_CLOCKS, loop=False, delay=83)
    pomo_cycle += 1
    display.show(Image.GHOST)
    audio.play(Sound.GIGGLE)

def timer_5():
    speech.say("Have a soda pop", speed=82, pitch=72, throat=110, mouth=105)
    music.play(music.POWER_UP)
    global pomo_cycle
    time = 5 * 60
    while time > 0:
        time -= 1
        #this animation should generate roughly one second of delay
        display.show(Image.ALL_CLOCKS, loop=False, delay=83)
    pomo_cycle += 1
    display.show(Image.GHOST)
    audio.play(Sound.GIGGLE)

def timer_15():
    speech.say("Go outside you bum", speed=82, pitch=72, throat=110, mouth=105)
    music.play(music.POWER_UP)
    global pomo_cycle
    time = 15 * 60
    while time > 0:
        time -= 1
        #this animation should generate roughly one second of delay
        display.show(Image.ALL_CLOCKS, loop=False, delay=83)
    display.show(Image.PACMAN)
    audio.play(Sound.SPRING)
    pomo_cycle = 1



while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake" and pomo_cycle == 1:
        display.scroll("pomo 1", 70)
        timer_25()
    elif gesture == "shake" and pomo_cycle == 2:
        display.scroll("break 1", 70)
        timer_5()
    elif gesture == "shake" and pomo_cycle == 3:
        display.scroll("pomo 2", 70)
        timer_25()
    elif gesture == "shake" and pomo_cycle == 4:
        display.scroll("break 2", 70)
        timer_5()
    elif gesture == "shake" and pomo_cycle == 5:
        display.scroll("pomo 3", 70)
        timer_25()
    elif gesture == "shake" and pomo_cycle == 6:
        display.scroll("break 3", 70)
        timer_5()
    elif gesture == "shake" and pomo_cycle == 7:
        display.scroll("pomo 4", 70)
        timer_25()
    elif gesture == "shake" and pomo_cycle == 8:
        display.scroll("big break", 70)
        timer_15()
