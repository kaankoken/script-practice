import threading
import random
import time

threadLock = threading.RLock()

#Lock example
class MyThreadClass(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name=thread_name)

    threadLock.acquire()   #It will lock when the other threads come here
                            #Only one threads come at a time 
    def run(self):
        print("Starting Point " + self.name)

        for i in range(3):
            time.sleep(2)
            print("{} {}\n".format(self.name, time.ctime(time.time())))

    threadLock.release()    #it will release when first thread's job is done 

def main():
    thread_1 = MyThreadClass("thread_1")
    thread_2 = MyThreadClass("thread_2")
    thread_3 = MyThreadClass("thread_3")
    
    #One at a time will be active
    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join( )
    thread_2.join() 
    thread_3.join()

if __name__ == "__main__":
    main()