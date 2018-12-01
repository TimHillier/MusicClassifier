import Classifier,Mine,DataProcess,sys,time
#ok whats the first thing we need?
def main():
    test_index = 123
    data,labels =  DataProcess.read_file(sys.argv[2])
    test_data = data[test_index]
    test_label = labels[test_index]
    del data[test_index]
    del labels[test_index]
    Classifier.support_vector_train(data,labels)
    Classifier.support_vector_classify(test_data,test_label)


#generates the data from all the wav files
def generate_data():
    t0 = time.time()
    DataProcess.find_songs(sys.argv[1])
    t1 = time.time()
    total = t1-t0
    print("DONE Processing:",total/60,"Minutes")


#mines the data given to it
def mine_data():
    Mine.mine("./data/Frames")

main()