from prent import Prent
from point import Point
import time

class ElevenDotEleven:
    waktu       = 0
    loop        = True

    easyTime    = 11
    normalTime  = 11.109999999999994
    hardTime    = 11.109999999999808
    maksWaktu   = 15

    point       = 0
    
    def __init__(self, level = "Anonim", mode = "Anonim"):
        self.level = level
        self.mode = mode
        
    def openingGamePlay(self):
        waktu = 3
        print("\n\n >>> Stand By \n\n")
        print(f" Game akan Dimulai dalam {waktu} detik !!! \n")
        while True:
            try:
                if waktu == 0:
                    break
            except(KeyboardInterrupt):
                Prent().stop()    
                exit()
            else:
                time.sleep(1)
            waktu -= 1

    def play(self):
        self.condition(self.level)
            
    def condition(self, level):
        if level == 1:
            sleeep      = 0.5
            plusTime    = 1
            targetTine  = self.easyTime

        elif level == 2:
            sleeep      = 0.1
            plusTime    = 0.11
            targetTine  = self.normalTime
            
        elif level == 3:
            sleeep      = 0.001
            plusTime    = 0.01
            targetTine  = self.normalTime

        self.run(sleeep=sleeep,plusTime=plusTime,targetTime=targetTine)

    def run(self, sleeep, plusTime, targetTime):
        self.openingGamePlay()
        self.waktu = 0

        while self.loop:
            #print(f"Waktu : {round(waktu, 4)}")
            if self.waktu >= self.maksWaktu:
                Prent().timeOut()
                break
            else:
                try:
                    if self.level == 1 or self.level == 2:
                        print("Waktu : {:.2f}".format(round(self.waktu, 3)))
                    elif self.level == 3:
                        print("Waktu : {:.2f}".format(round(self.waktu, 4)))
                    time.sleep(sleeep)
                except(KeyboardInterrupt):
                    self.stop(targetTime)
                    break
                else:
                    self.waktu += plusTime

    def stop(self, targetTime = 0):
        if self.waktu == targetTime:
            self.point += 1
            if self.mode == 1:
                Prent().end()
            elif self.mode == 2 or self.mode == 3:
                Prent().good()
        else:
            if self.mode == 1:
                Prent().end()
            elif self.mode == 2:
                Prent().bad()
            else:
                Prent().end()
        