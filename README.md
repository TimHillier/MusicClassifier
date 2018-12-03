# Music Classifier Using Data Mining and Machine Learning

A music classifier in Python for CPSC 473.

Written in Python 3.6

# Basic Information

I cut all songs down into 30 second .wav files using ffmpeg. I then used Marsyas to collect Mel-frequency cepstrual 
coefficients, from the 30 second clips. MFCCs are coefficients that represent the short-term power spectrum of a sound. 
Putting the MFCC vectors into a SVM I was able to classify different genres of music.  
 
I've included test data with a different number of genres so that you do not have to collect your own.

# Results
After running the classifier with different number of genres we can see that after 4-5 genres the classifier starts to
decline in accuracy.

| Number of Genres 	| % Correct 	| % Wrong 	|
|:----------------:	|:---------:	|:-------:	|
|         2        	|   92.5%   	|   7.5%  	|
|         3        	|    68%    	|   32%   	|
|         4        	|    60%    	|   40%   	|
|         5        	|    62%    	|   38%   	|
|         7        	|    46%    	|   53%   	|
|        10        	|    43%    	|   56%   	|





# Install Requirements
```
pip install -r requirements.txt 
```

Run the code
```
python Main.py <Path/To/.arff>
```

# Regarding the .arff file

To generate a .arff file I used [Marsyas](http://marsyas.info/) to get the Mel-frequency cepstral coeffcients in a .arff file, in a single
vector.

# Improvements


# Trouble Shooting
problem with tkinter not being installed? try
```
sudo apt-get install python3-tk
```

Use ffmpeg to convert mp3 to 30 second wav
```
ffmpeg -ss 00:00:30 -t 00:00:30 -i  <song.mp3> <song.wav>
```


# References
[1] R. Griesmeyer, "Music Recommendation and Classification Utilizing Machine Learning and Clustering Methods." (2011).
Florida State University.

[2] M. Haggblade, Y. Hong, K. Kao "Music Genre Classification" (2011).

[3] T. Li, L. Li "Music Data Mining: An Introduction" (2010)

[4] Y. Costa, L. Oliveira, C. Silla Jr. "An evaluation of convolutional Neural Networks for music classification using 
Spectrograms" (2016)



