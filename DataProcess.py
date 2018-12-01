#process the data for classification
import os,wave,sys,pylab,struct,arff
import numpy as np
from progress.bar import Bar
from scipy.io import arff
from io import StringIO
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


#if this works i wont need anything above.
#reads the .arff file
def read_file(file_to_read):
    #the file should be a .arff file
    if(not(file_to_read.endswith('.arff'))):
        print("File Should end with .arff")
        quit(0)
    # file = arff.load(open(file_to_read),'rb')
    f = StringIO(file_to_read)
    data,meta = arff.loadarff(f)
    # data = file["data"]
    # out = file["attributes"][-1] #good
    print(meta)


