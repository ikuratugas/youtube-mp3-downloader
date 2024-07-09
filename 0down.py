import os
from pytube import YouTube
from pydub import AudioSegment


url = input('Masukkan Link Youtube: ')

my_video = YouTube(url)

judul = my_video.title.replace(".", "").replace("//", "").replace("'", "").replace("/", "").replace(",", "").replace(
    "  ", "").replace("|", "").replace("[", " ").replace("]", " ").replace("#", "").replace("   ", "").replace(":", "")
print(my_video.title)

my_video = my_video.streams.get_audio_only()

my_video.download()


audio = AudioSegment.from_file(f"{str(judul)}.mp4", "mp4")
audio.export(f"{str(judul)}.mp3", format="mp3")

os.remove(f"{judul}.mp4")
