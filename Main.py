import Classifier,Mine,DataProcess,sys
#ok whats the first thing we need?
def main():
    DataProcess.find_songs(sys.argv[1])
    print("DONE")

main()