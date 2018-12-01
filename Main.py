import Classifier,Mine,DataProcess,sys,time
#ok whats the first thing we need?
def main():
    # generate_data()
    # mine_data()
    print("trying",sys.argv[2])
    DataProcess.read_file(sys.argv[2])



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