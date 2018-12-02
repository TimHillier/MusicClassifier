#classifying
from sklearn import svm

clf = svm.SVC(gamma='scale')

def support_vector_train(_X,_Y):
    clf.fit(_X,_Y)


def support_vector_classify(test_data,test_labels):
    results = []
    for i in range(0,len(test_data)):
        answer = clf.predict([test_data[i]])[0]
        # print("Actual:",test_labels[i]," Classified as:",answer)
        results.append([test_labels[i],answer])
    percentage_correct(results)


#tells us the percentage correct
def percentage_correct(classified_results):
    total = len(classified_results)
    correct = 0
    wrong = 0
    for x in classified_results:
        if x[0] == x[1]:
            correct += 1
        else:
            wrong += 1
    print(str((correct/total * 100)) + "% correct:",correct,"/",total )
    print(str((wrong/total * 100)) + "% wrong:",wrong,"/",total)
