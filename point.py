import time
from prent import Prent

class Point:
    def __init__(self, point) -> None:
        self.point = point

    def conditionEnd(self, mode, level, value = 0):
        modee = {1: "Normal", 2: "Costum", 3:"Endless"}
        levell = {1: "Easy", 2 : "Normal", 3: "Hard"}
        mode = modee[int(mode)]
        level = levell[int(level)]
        
        self.end(mode, level, value)
    
    def end(self, mode, level, value):
        try:
            Prent().loadingSkor()
        except(KeyboardInterrupt):
            Prent().stop()
            exit()
        else:
            print(f">> Mode Game        : {mode}")
            print(f">> Level Game       : {level}")
            if mode == "Endless":
                print(f">> Total Game       : {self.point + 1}")
            elif mode == "Costum":
                print(f">> Total Pengulangan: {value}")
            if mode != "Normal":
                print(f">> Skor             : {self.point} \n\n\n")
            else:
                if self.point == 1:
                    Prent().win()
                else:
                    Prent().lose()