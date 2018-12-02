# Music Classifier Using Data Mining and Machine Learning

A music classifier in Python for CPSC 473

#Start Information

I cut all songs down into 30 second .wav files.
This can be accomplished with ffmpeg. 

```
pip install -r requirements.txt 
```

Run the code
```
python Main.py <Path/To/.arff>
```

#Regarding the .arff file

To generate a .arff file I used "marsyas" to get the Mel-frequency cepstral coeffcients in a .arff file.


# Trouble Shooting
problem with tkinter not being installed? try
```
sudo apt-get install python3-tk
```

Use ffmpeg to convert mp3 to 30 second wav
```
ffmpeg -ss 00:00:30 -t 00:00:30 -i  <song.mp3> <song.wav>
```

#Refrences
