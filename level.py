from prent import Prent

class Level:
    def choiceLevel(self):
        while True:
            try:
                level = input("Pilih Level : [Easy/Normal/Hard] \n > ").capitalize()
            except(KeyboardInterrupt):
                Prent().stop()
                exit()
            else:
                if level == "Easy":
                    level = 1
                    break
                if level == "Normal":
                    level = 2
                    break
                elif level == "Hard":
                    level = 3
                    break
                else:
                    continue
        return level