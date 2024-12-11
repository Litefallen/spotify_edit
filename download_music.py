import os
import pytube
from os import path

# Function to create the 'Music' folder if it doesn't exist and set it as the current working directory
def folder_mk():
    cur_dir = os.getcwd()
    if not path.split(cur_dir)[1] == 'Music':
        if not os.path.exists('Music'):
            os.mkdir('Music')
    os.chdir("Music")

async def symbols_check(letter: str) -> str:
    return ''.join([i if i.isalnum() else '_' for i in letter])


async def get_your_music(artist: str, song: str):
    artist = await symbols_check(artist)
    song = await symbols_check(song)
    print(artist,song)
    if not os.path.exists(f"{artist}_{song}"):
        res_song = pytube.Search(f'{artist} - {song} audio')
        rev_res = res_song.results[0]
        rev_res2 = rev_res.streams.filter(adaptive=True).filter(only_audio=True)
        best_quality = rev_res2.order_by('abr')[-1]
        # print(best_quality.title)
        # print(f"This is the file's name:{artist}_{song}")
        best_quality.download(filename=f"{artist}_{song}")
    else: print('This song is downloaded already')







