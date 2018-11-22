#process the data for classification
import os,wave,sys,pylab
import numpy as np
from progress.bar import Bar
from matplotlib import mlab,pyplot

#get songs from destination
def find_songs(DataFolder):
    check_output("./Spect")
    files = os.listdir(DataFolder)
    bar = Bar('Generating Spectrograms',max = len(files))
    for i in range(len(files)):
        generate_spectrogram(DataFolder+"/"+files[i],"./Spect")
        bar.next()
    bar.finish
    #this is where you put loading bar


def check_output(outputdirectory):
    try:
        os.mkdir(outputdirectory)
    except:
        pass




#generate Spectrogram for the current song
def generate_spectrogram(song,outputdirectory):
    sound_info,frame_rate = get_wave_info(song)
    pylab.figure(num=None, figsize=(19,12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r'% song)
    pylab.specgram(sound_info,Fs=frame_rate)
    pylab.savefig(outputdirectory+"/"+((song.split("/")[-1]).split(".")[0])+".png")

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
