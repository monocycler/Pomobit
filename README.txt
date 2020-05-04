Pomobit - Pomodoro Technique on a BBC micro:bit
(c) Barry Prescott 2020
=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Developed at https://python.microbit.org/v/2.0
Non-blocking, so button presses always work. 
Press A to START or RESTART at any time
Press B to RESET at any time
Connect GND to gnd of a piezo buzzer and connect pin0 to + of buzzer 
See https://support.microbit.org/support/solutions/articles/19000101901-connecting-a-speaker-to-the-micro-bit
=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from microbit import *
import music
import speech

speech.say('Hello, World')
UPDATE_INTERVAL = 3000 #300000ms=>tick every 5 mins, Use 3000ms to accelerate for testing.

display.show(Image('09990:'
                   '99999:'
                   '99999:'
                   '99999:'
                   '09990'))
timer_start = 0
n=0

while True:
  if button_a.was_pressed(): #start or restart 
    timer_start = running_time()
    next_update = running_time() + UPDATE_INTERVAL
    n=0
    speech.say('Go')
    display.show(Image('00900:'
                       '00900:'
                       '00900:'
                       '00000:'
                       '00000'))
  if button_b.was_pressed(): #reset 
    timer_start = 0
    n=0
    display.show(Image('09990:'
                       '99999:'
                       '99999:'
                       '99999:'
                       '09990'))
  if ((timer_start != 0) and (running_time() > next_update)):
    n=n+5
    next_update = running_time() + UPDATE_INTERVAL
    if n>25: #=30 break finished - RESET
      display.show(Image('09990:'
                         '99999:'
                         '99999:'
                         '99999:'
                         '09990'))
      music.play(music.BA_DING)
      timer_start = 0
      n=0
    elif n>20: #=25
      display.show(Image('00000:'
                         '00000:'
                         '00900:'
                         '00900:'
                         '00090'))
      music.play(music.RINGTONE)
      speech.say('Take a break')
      display.scroll('Break', wait=False) # 5 .. 10 .. 15 .. 20 .. 25
    elif n>15: #=20
      display.show(Image('00000:'
                         '00000:'
                         '00990:'
                         '00009:'
                         '00000'))
    elif n>10: #=15
      display.show(Image('00000:'
                         '00000:'
                         '00999:'
                         '00000:'
                         '00000'))
    elif n>5: #=10
      display.show(Image('00000:'
                         '00009:'
                         '00990:'
                         '00000:'
                         '00000'))
    elif n>0: #=5
      display.show(Image('00090:'
                         '00900:'
                         '00900:'
                         '00000:'
                         '00000'))
