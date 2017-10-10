from ffmpy import FFmpeg, FFprobe
import time
import re
import subprocess 

log_mode = "debug"


class Song:

    def __init__(self, filename):
        self.filename = filename
        self.artist = None
        self.title = None
        self.genre = None
        self.duration = None
        self.bitrate = None

    def get_info(self):
        ff = FFprobe(inputs = {self.filename: None}) 
        info = ff.run(stderr=subprocess.PIPE)
        ## Parse Info 
        self.bitrate = re.search(".?bitrate:\s([0-9]*)\skb/s", str(info)).group().strip()
    
    def convert_to_mp3(self):
        filename_no_extension, extension = self.filename.split('.')
        timestamp = time.time()
        output = filename_no_extension + "_" + str(timestamp) + ".mp3"
        ff_convert({self.filename: None}, {output: None})
        self.filename = output

    def convert_to_wav(self):
        filename_no_extension, extension = self.filename.split('.')
        timestamp = time.time()
        output = filename_no_extension + "_" + str(timestamp) + ".wav"
        ff_convert({self.filename: None}, {output: None})
        self.filename = output

class MP3(Song):
    pass

class WAV(Song):
    pass
 

def ff_convert(inputs, outputs):
    ff = FFmpeg(inputs = inputs, outputs = outputs)
    if log_mode == "debug": print ff.cmd
    ff.run()
    

def get_songs_from_file(filename):
    pass    

def get_song_from_mp3_file(filename):
    return Song(filename)

if __name__ == "__main__":
    song = get_song_from_mp3_file("songs/Revive.mp3")
    #song.convert_to_mp3()
    #song.convert_to_wav()
    print song.bitrate    
    song.get_info()
    print song.bitrate






