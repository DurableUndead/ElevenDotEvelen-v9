from elevendoteleven import ElevenDotEleven
from point import Point
from level import Level
from mode import Mode
from info import Info
from prent import Prent

import time
import os

class Game:
    maksCostum  = 10
    MinCostum   = 1

    def play(self):
        level = Level()
        mode = Mode()
        valueLevel  = level.choiceLevel()
        valueMode   = mode.choiceMode()
        self.conditionGame(mode=valueMode, level=valueLevel)

    def conditionGame(self, mode, level):
        game = ElevenDotEleven(level, mode)

        if level == 1:
            if mode == 1:
                game.play()
            elif mode == 2:
                valueCostum = self.costum()
                for i in range(valueCostum):
                    game.play()
                    if i + 1 == valueCostum:
                        Prent().end()
            elif mode == 3:
                while True:
                    game.play()
                    if game.waktu != game.easyTime:
                        break

        elif level == 2:
            if mode == 1:
                game.play()
            elif mode == 2:
                valueCostum = self.costum()
                for i in range(valueCostum):
                    game.play()
                    if i + 1 == valueCostum:
                        Prent().end()
            elif mode == 3:
                while True:
                    game.play()
                    if game.waktu != game.normalTime:
                        break

        elif level == 3:
            if mode == 1:
                game.play()
            elif mode == 2:
                valueCostum = self.costum()
                for i in range(valueCostum):
                    game.play()
                    if i + 1 == valueCostum:
                        Prent().end()
            elif mode == 3:
                while True:
                    game.play()
                    if game.waktu != game.hardTime:
                        break
        
        if mode == 2:
            Point(point=game.point).conditionEnd(mode=mode,level=level, value=valueCostum)
        else:
            Point(point=game.point).conditionEnd(mode=mode,level=level)
        self.again()

    def again(self):
        try:
            time.sleep(2)
            while True:
                try:
                    playAgain = input("Ingin Bermain lagi? [Ya/Tidak] \n > ").capitalize()
                except(KeyboardInterrupt):
                    Prent().stop()     
                    exit()
                else:
                    if playAgain == "Ya":
                        ElevenDotEleven().point = 0
                        break
                    elif playAgain == "Tidak":
                        self.quitGame()
                    else:
                        print()
                        continue
        except(KeyboardInterrupt):
            Prent().stop()     
            exit()

    def costum(self):
        while True:
            try:
                costum = int(input("Masukan banyak Pengulangan : \n > "))
            except(KeyboardInterrupt):
                Prent().stop()
                exit()
            else:
                if self.MinCostum <= costum <= self.maksCostum:
                    break
                else:
                    print(f"Minimal dalam Mode Costum = {self.MinCostum}\nMaksimal dalam Mode Costum = {self.maksCostum}\n")
                    time.sleep(1)
                    continue
        return costum

    def menu(self):
        while True:
            Prent().opening()
            try:
                print("Pilih Menu : ")
                ychoice = int(input(" > "))
            except(KeyboardInterrupt):
                Prent().stop()     
                exit()
            except(ValueError):
                continue
            else:
                if ychoice == 1:
                    self.play()
                elif 1 < ychoice < 5:
                    Info(choice=ychoice)
                    while True:
                        try:
                            time.sleep(0.5)
                            back = input("Ingin kembali ke Menu? [Ya/Tidak] \n > ").capitalize()
                        except(KeyboardInterrupt):
                            Prent().stop()       
                            exit()
                        else:
                            if back == "Ya":
                                print(os.system("cls"))
                                break
                            elif back == "Tidak":
                                self.quitGame()
                            else:
                                continue
                elif ychoice == 5:
                    self.quitGame()
                else:
                    continue

    def quitGame(self):
        Prent().quit()
        exit()