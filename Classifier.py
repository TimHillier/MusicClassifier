#classifying
from sklearn import svm
import pandas

#brain of the SVM
clf = svm.SVC(gamma='scale')

#train the SVM
def support_vector_train(_X,_Y):
    clf.fit(_X,_Y)


#after Training the SVM Classify some test data and see if it is correct
def support_vector_classify(test_data,test_labels):
    results = []
    for i in range(0,len(test_data)):
        answer = clf.predict([test_data[i]])[0]
        results.append([test_labels[i],answer])
    percentage_correct(results)


#tells us the percentage correct
def percentage_correct(classified_results):
    belief_table = {}
    total = len(classified_results)
    correct = 0
    wrong = 0
    for x in classified_results:
        out = str(x[0]) + " as " + str(x[1])

        if out in belief_table:
            belief_table[out] = belief_table.get(out) + 1
        else:
            belief_table.update({out:1})

        if x[0] == x[1]:
            correct += 1
        else:
            wrong += 1
    #lets output this to a file
    print_to_file(correct,wrong,total,belief_table,"Classification_Results.txt")


#prints the information to a file
def print_to_file(correct,wrong,total,belief_table,file_name):
    file = open(file_name,"w+")
    file.write(str(pandas.DataFrame.from_dict(belief_table,orient='index',columns=["Times Classified As"])))
    file.write("\n-------------------------------\n")
    file.write(str((correct/total)*100) + "% correct: " + str(correct) + "/" + str(total) + "\n")
    file.write(str((wrong/total)*100) + "% wrong: " + str(wrong) + "/" + str(total) + "\n")
    print(str((correct/total * 100)) + "% correct:",correct,"/",total)
    print(str((wrong/total * 100)) + "% wrong:",wrong,"/",total)
    print(pandas.DataFrame.from_dict(belief_table,orient='index',columns=["Times Classified As"]))
    print("\nInformation written to file:",file_name)
