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
    sound_info = pylab.fromstring(frames,'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info,frame_rate


#reads the .arff file
def read_file(file_to_read):
    _X = []
    _Y = []
    test_X = []
    test_Y = []
    #the file should be a .arff file
    if(not(file_to_read.endswith('.arff'))):
        print("File Should end with .arff")
        quit(0)
    data, meta = arff.loadarff(file_to_read)
    #if i get every 5th element it should be 20% of the total
    counter = 0
    split = 4
    for i in range(0,len(data)):
        data_list = data[i].tolist()
        data_list = list(data_list)
        label = data_list[-1].decode('utf-8')
        del(data_list[-1])
        if counter == split:
            test_X.append(data_list)
            test_Y.append(label)
            counter = 0
        else:
            _X.append(data_list)
            _Y.append(label)
            counter += 1
    return _X,_Y,test_X,test_Y