import threading
import random
import time

class SemaphoreThread(threading.Thread):
    available_table =  ["A", "B", "C", "D", "E"]
    
    def __init__(self, thread_name, semaphore):
        threading.Thread.__init__(self, name=thread_name)
        self.sleep_time = random.randrange(2,6) 
        self.semaphore = semaphore 

    def run(self):
        self.semaphore.acquire()
        table = SemaphoreThread.available_table .pop()
        print("{} entered and seated at table {}".format(self.name, table))
        
        time.sleep(self.sleep_time)
        print("{} is exiting  now and freeing table {}".format(self.name, table))
        self.available_table.append(table)

        self.semaphore.release ()


#it uses counter 
def main():
    threads = []
    semaphore = threading.Semaphore(len(SemaphoreThread.available_table))

    for i in range(1, 11):
        threads.append(SemaphoreThread("thread_" + str (i), semaphore))
    
    for thread in threads:
        thread.start() 

if __name__ == "__main__":
    main()