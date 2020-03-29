import threading
import time
import random

class FlagThread(threading.Thread):
    def __init__(self, thread_name, event):
        threading.Thread.__init__(self, name=thread_name)
        self.event = event
 
    def run(self):
        time.sleep(random.randint(1,10))
        print("{} arrived at {}".format(self.name, time.ctime(time.time())))
        self.event.wait()
        print("{} passess through intersection at {}".format(self.name, time.ctime(time.time())))

def main():
    green_light = threading.Event()
    vehicles = []

    for i in range(1, 11):
        vehicles.append(FlagThread("Vehicle " + str(i), green_light))
    
    for vehicle in vehicles:
        vehicle.start()
    
    while threading.activeCount() > 1:
        #means red light 
        green_light.clear()
        print("RED light")
        time.sleep(3)

        green_light.set()
        print("GREEN light")
        time.sleep(2)

if __name__ == "__main__":
    main()