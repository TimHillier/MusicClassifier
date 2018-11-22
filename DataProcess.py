#process the data for classification
import progress,os,wave,sys,pylab
import numpy as np
from matplotlib import mlab,pyplot

#get songs from destination
def FindSongs(DataFolder):
    #this is where you put loading bar
    os.chdir(DataFolder)
    print("Current Directory", os.getcwd())
    print(os.listdir(DataFolder))





#generate Spectrogram for the current song
def generate_spectrogram(song):
    sound_info,frame_rate = get_wave_info(song)
    pylab.figure(num=None, figsize=(19,12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r'% song)
    pylab.specgram(sound_info,Fs=frame_rate)
    pylab.savefig(((song.split("/")[-1]).split(".")[0])+".png")

#gets info about the song
def get_wave_info(song):
    wav = wave.open(song,"r")
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames,'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info,frame_rate


#if the song is not wav turn it into wav
def file_to_wav(song):
    print("file to wave")
