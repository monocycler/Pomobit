from microbit import *
import music
import speech

speech.say('Hello, World')
UPDATE_INTERVAL = 300000 #300000ms=>tick every 5 mins, 3000ms is accelerated to test.

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
