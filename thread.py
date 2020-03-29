import threading
import random
import time

class PrintThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self,name=thread_name)
        self.sleep_time = random.randrange(2,6)
    
    def run(self):
        time.sleep(self.sleep_time)
        print("{} thread is completed\n".format(self.name))

def main():
    #Born State
    thread_1 = PrintThread("thread_1")
    thread_2 = PrintThread("thread_2")
    thread_3 = PrintThread("thread_3")

    #Ready State
    #Run method will be invoked
    thread_1.start()
    thread_2.start()
    thread_3.start()

    '''
        Program can be completed without waiting threads
        if we do not have join methods.
 
        If we have join methods, program needs to wait
        until the threads completed 
    '''
    thread_1.join()
    thread_2.join() 
    thread_3.join()