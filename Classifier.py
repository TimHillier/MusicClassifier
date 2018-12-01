#classifying
from sklearn import svm

clf = svm.SVC(gamma='scale')

def support_vector_train(_X,_Y):
    clf.fit(_X,_Y)


def support_vector_classify(test_data,test_labels):
    for i in range(0,len(test_data)):
        print("should be ",test_labels[i],"is",clf.predict([test_data[i]]))

