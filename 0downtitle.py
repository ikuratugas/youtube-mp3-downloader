import os
from pytube import YouTube
from pydub import AudioSegment


url = input('Masukkan Link Youtube: ')
print(" ^^^^^^^^^^^^^^ ")
title = input('Masukkan judul lagu: ')


my_video = YouTube(url)

judul = title

my_video.title = judul
my_video = my_video.streams.get_audio_only()

my_video.download()


audio = AudioSegment.from_file(f"{str(judul)}.mp4", "mp4")
audio.export(f"{str(judul)}.mp3", format="mp3")

os.remove(f"{judul}.mp4")
