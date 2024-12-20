
#Process - instance of a program
## multithreading
## 1. IO bound task
## 3. Concurrent Execution

## multiprocess - processes that are run in parallel

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(.1)
        print(i)

def print_letters():
    for letter in "Hello Brother":
        time.sleep(1)
        print(letter)

if __name__=='__main__':
    t1 = threading.Thread(target=print_numbers())
    t2 = threading.Thread(target=print_letters())

    t = time.time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    finished_time = time.time() - t
    print(finished_time)