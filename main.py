from os import listdir
from os.path import isfile, join
from pygame import mixer as p
import random as r
playlist_dir='/home/gxman/Documents/code/mp3 player/music'
#playlist_dir='/home/gxman/Music/shellbeats/school/'
songs=[]
songs_preshuffle=[]

def start_up():
    p.init()
def change_song_to_play(current_song):
    global next_song
    global previous_song
    next_song = (current_song + 1) % len(songs)
    previous_song = (current_song - 1) % len(songs)
def play_songs(song_index):
    p.music.load(songs[song_index])
    change_song_to_play(song_index)
    p.music.play()
def load_playlist(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return [join(path, f) for f in sorted(files)]
def pause():
    if p.music.get_busy():
        p.music.pause()
    else:
        p.music.unpause()
def next():
    p.music.unload()
    play_songs(next_song)
def previous():
    p.music.unload()
    play_songs(previous_song)
def toggle_shuffle():
    global songs
    global songs_preshuffle
    if songs_preshuffle==[]:
        songs_preshuffle=songs
        r.shuffle(songs)
    elif songs_preshuffle !=[]:
        songs=songs_preshuffle
        songs_preshuffle=[]
    else:
        raise SyntaxError

def menu():
    global songs
    songs=load_playlist(playlist_dir)
    song_to_play=0
    play_songs(song_to_play)
    while True:
        userin=input()
        if userin == "":
            pause()
        elif userin=="n":
            next()
        elif userin=="p":
            previous()
        elif userin=="s":
            toggle_shuffle()
if __name__=="__main__":
    start_up()
    menu()
