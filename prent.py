import os
import time

class Prent:  
    def opening(self):
        print(os.system("cls"))
        print("""
            ElevenDotEleven (11.11)
                    versi 9
    
1) Play Game
2) Info Game
3) Info Level and Mode
4) About
5) Quit Game
""")

    def good(self):
        print("\n\n\n >>> GGWP !!! \n\n\n")
        time.sleep(1)

    def bad(self):
        print("\n\n\n >>> Semangat !!! \n\n\n")

    def win(self):
        print("\n>>> Selamat, Kamu Menang !!! \n\n\n")

    def lose(self):
        print("\n>>> Sayang sekali, kamu gagal \n\n\n")
    
    def timeOut(self):
        print("\n\n\n >>> Waktu Habis")

    def end(self):
        print("\n\n\n >>> Game Berakhir \n")
    
    def loadingSkor(self):
        print("\n >>> Loading Skor\n")
        time.sleep(2)

    def stop(self):
        print("\n\n\n >>> Program dihentikan \n\n\n")
        time.sleep(1)
    
    def quit(self):
        print("\n\n\n >>> Good Bye\n\n\n")
        time.sleep(1)
