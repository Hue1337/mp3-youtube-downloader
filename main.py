# Author:
#   https://github.com/Hue1337
#   Software was made for educational purpose only!
#   Only non-commercial usage allowed!


import os

from pytube import YouTube 
from moviepy.editor import * 

print('YouTube url:\nHue@1337> ', end='')
url = input()
yt = YouTube(url)

stream = yt.streams.filter(only_audio=True).first()
stream.download()




def mp4_to_mp3(mp4FILE, mp3FILE):

    mp4_without_frames = AudioFileClip(mp4FILE)     
    mp4_without_frames.write_audiofile(mp3FILE)     
    mp4_without_frames.close() 


for file in os.listdir():

    if '.mp4' in file:

        mp4_to_mp3(file, file[:len(file)-3]+'mp3')
        com = 'rm "'+str(file)+'"'
        os.system(com)

