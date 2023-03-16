from prent import Prent

class Mode:
    def choiceMode(self):
        while True:
            try:
                mode = input("Pilih Mode  : [Normal/Costum/Endless] \n > ").capitalize()
            except(KeyboardInterrupt):
                Prent().stop()
                exit()
            else:
                if mode == "Normal":
                    mode = 1
                    break
                elif mode == "Costum":
                    mode = 2
                    break
                elif mode == "Endless":
                    mode = 3
                    break
                else:
                    continue
        return mode