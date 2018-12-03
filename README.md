# Music Classifier Using Data Mining and Machine Learning

A music classifier in Python for CPSC 473.

#Start Information

I cut all songs down into 30 second .wav files.
This can be accomplished with ffmpeg.
 
I've included test data so that you do not have to collect your own.


#Install Requirements
```
pip install -r requirements.txt 
```

Run the code
```
python Main.py <Path/To/.wavs> <Path/To/.arff>
```

#Regarding the .arff file

To generate a .arff file I used "Marsyas" to get the Mel-frequency cepstral coeffcients in a .arff file.

#Improvements
1. Better Output. Make the output more clear and more informative. Maybe what the incorrect songs are classified as. 


# Trouble Shooting
problem with tkinter not being installed? try
```
sudo apt-get install python3-tk
```

Use ffmpeg to convert mp3 to 30 second wav
```
ffmpeg -ss 00:00:30 -t 00:00:30 -i  <song.mp3> <song.wav>
```


#References
[1] R. Griesmeyer, "Music Recommendation and Classification Utilizing Machine Learning and Clustering Methods." (2011).
Florida State University.

[2] M. Haggblade, Y. Hong, K. Kao "Music Genre Classification" (2011).

[3] T. Li, L. Li "Music Data Mining: An Introduction" (2010)

[4] Y. Costa, L. Oliveira, C. Silla Jr. "An evaluation of convolutional Neural Networks for music classification using 
Spectrograms" (2016)



