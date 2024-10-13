from music import MusicBot as MB
import time

def download_song(pesma):
   with MB() as bot:
            bot.land_first_page()
            bot.search_song(song=pesma)
            bot.find_first_video(song=pesma)
            bot.download_video()
            time.sleep(5)

with open("playlista\\pesme.txt", "r") as file:
    pesme = file.readlines()
    list = [pesma.strip("\n") for pesma in pesme]

    for pesma in list:
        download_song(pesma)
     


    