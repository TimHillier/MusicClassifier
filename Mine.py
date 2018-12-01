#the Mining Portion of this project
import pyfpgrowth,os




#Mine the data from the path
def mine(path):
    file_names = os.listdir(path)
    file = open(path+"/"+file_names[0],"r")
    print(file.readline())
