#process the data for classification
import os,wave,sys,pylab,struct
import numpy as np
from progress.bar import Bar
from matplotlib import mlab,pyplot

#get songs from destination
def find_songs(DataFolder):
    setup()
    files = os.listdir(DataFolder)
    bar = Bar('Generating Spectrograms',max = len(files))
    for i in range(len(files)):
        generate_spectrogram(DataFolder+"/"+files[i],"./data/Spect")
        bar.next()
    bar.finish
    #this is where you put loading bar

#check to see if the output directory Exists
def check_output(outputdirectory):
    try:
        os.mkdir(outputdirectory)
    except:
        pass

#setup and check to make sure that the folders you need actually exist
def setup():
    check_output("./data")
    check_output("./data/Spect")
    check_output("./data/Frames")
    check_output("./data/Misc")


#generate Spectrogram for the current song
def generate_spectrogram(song,outputdirectory):
    sound_info,frame_rate = get_wave_info(song)
    filename = ((song.split("/")[-1]).split(".")[0])
    title = outputdirectory+"/"+ filename
    pylab.figure(num=None, figsize=(19,12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r'% song)
    data = pylab.specgram(sound_info,Fs=frame_rate)  #so this i need to output to file...
    output_to_file(data,"./data/Misc/"+filename)
    pylab.savefig(title + ".png")

#output data to file for data mining, not picture
def output_to_file(data,file):
    with open(file+".txt",'w+') as f:
        i = 0
        for item in data:
            i += 1
            f.write("%s," % item)
            if(i == 30):
                f.write("\n")
                i = 0



#gets info about the song
def get_wave_info(song):
    wav = wave.open(song,"r")
    frames = wav.readframes(-1)
    output_to_file(frames,"./data/Frames/"+(song.split("/")[-1]).split(".")[0]+"_frames")
    # thing = map(ord,frames)
    sound_info = pylab.fromstring(frames,'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info,frame_rate


#if the song is not wav turn it into wav
#this is just a bash script using ffmpeg
def file_to_wav(song):
    print("file to wave",song)
