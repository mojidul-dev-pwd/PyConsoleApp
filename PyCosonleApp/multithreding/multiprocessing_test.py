import multiprocessing
import time

def print_square():
    for i in range(5):
        time.sleep(1)
        print("Process 1-->"+str(i*i))

def print_cube():
    for i in range(5):
        time.sleep(1)
        print("Process 2-->"+str(i * i * i))

if __name__=='__main__':
    p1 = multiprocessing.Process(target=print_square)
    p2 = multiprocessing.Process(target=print_cube)
    t = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)