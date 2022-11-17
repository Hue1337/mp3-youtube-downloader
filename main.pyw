import argparse
from pytube import YouTube

def mp3():
    print('mp3')

def mp4():
    print('mp4')

parse = argparse.ArgumentParser()

parse.add_argument('h',     help='Handbook of using mp3-yt-downloader.')
parse.add_argument('mp3',   func=mp3   ,help='Download video in mp3 (only audio) format.')
parse.add_argument('mp4',   func=mp4   ,help='Donwload a video in mp4 (video+audio) format.')
parse.add_argument('a'   ,help='The author: https://github.com/Hue1337')




# if __name__ == '__main__':

