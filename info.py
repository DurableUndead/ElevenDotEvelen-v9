class Info:
    def __init__(self, choice) -> None:
        acc = {
            2: self.infoGame,
            3: self.infolevel,
            4: self.about
        }
        acc[int(choice)]()
    
    def infoGame(self):
        print("""
                    One Quadruple / ElevenDotEleven (11.11)
                          versi 9 (Asparagus Artemis)
                           (gk tau kasih nama apaan)

    Game dengan mengandalkan kehokian dan ketepatan dalam memberhentikan waktu.
ketika Game di run, cukup berhentikan Game dengan menekan tombol pada keyboard
>>> ctrl + c
Game harus diberhentikan ketika waktu berhenti tepat di angka '11.11'. (Kecuali level Easy)
untuk info lebih lanjut, lihat di 'Info Level dan Mode'
        """)

    def infolevel(self):
        print("""

Level : 1.Easy      (waktu ditambahkan 1 dengan speed 0.5/s) <- New Level (BETA)
        2.Normal    (waktu ditambahkan 0.11 dengan speed 0.1/s)
        3.Hard      (waktu ditambahkan 0.01 dengan speed 0.001/s)

Mode  : 1.Normal    (1x kali percobaan)
        2.Costum    (Bisa memilih berapa banyak percobaan) <--- New Mode (BETA)
        3.Endless   (Jika tepat memberhentikan waktu diangka 11.11,
                        game akan auto mengulang sampai gagal/kalah)

Catatan : 1. Dalam level Easy, Waktu harus berhenti tepat di angka '11' bukan '11.11'
          2. Hanya Mode 2 dan 3 dapat melihat Skor
          3. Jika menekan 'ctrl + c' dalam Loading ataupun dalam Menu, 
             Program akan Berhenti

        """)
    
    def about(self):
        print("""

Developed By  : 
    # Alfiansyah Achmad
    # UBSI - Ilmu Komputer
    # Semester 1

Software        : 
    # Visual Studio

Reference       :
    # From a Japanese video about girls participating in the pocky game "11.11",
      by pressing the button so that the time stops right at 11.11
    # Link Video : https://www.instagram.com/reel/CWfP40tlE5x/?utm_medium=copy_link

Thanks          :
    # Andrien Wiandyano (Comment)

        """)