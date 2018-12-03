#process the data for classification
import arff
from scipy.io import arff

"""
Preprocess the data
reads the .arff file and sends it to the SVM
Uses 80% to train the classifier and 
Uses 20% to test the classifier
"""
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
    return _X, _Y, test_X, test_Y


