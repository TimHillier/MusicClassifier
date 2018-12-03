import Classifier,DataProcess,sys,time
#ok whats the first thing we need?
def main():
    data,labels,test_data,test_label =  DataProcess.read_file(sys.argv[1])
    Classifier.support_vector_train(data,labels)
    Classifier.support_vector_classify(test_data,test_label)

main()