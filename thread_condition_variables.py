import threading
import time

#zero means no resource
resource_is_available = 0
 
class ConsumerThread(threading.Thread):
    def __init__(self, condition, thread_name):
        threading.Thread.__init__(self, name=thread_name)
        self.condition = condition
        print("Consumer {} has been generated".format(self.name))

    def run(self):
        global resource_is_available
        with self.condition:
            while resource_is_available == 0:
                print("Consumer {} is waiting".format(self.name))
                self.condition.wait()
            print("Resource has been consumed by {}".format(self.name))
            resource_is_available = 0

class ProducerThread(threading.Thread):
    def __init__(self, condition):
        threading.Thread.__init__(self)
        self.condtion = condition
        print("Producer has been generated")
    
    def run(self):
        global resource_is_available
        for i in range(5):
            with self.condtion:
                resource_is_available = 1
                self.condtion.notifyAll()
            time.sleep(5)

def main():
    condition = threading.Condition()
    producer = ProducerThread(condition)

    consumer_thread_1 = ConsumerThread(condition=condition, thread_name="consumer_thread_1")
    consumer_thread_2 = ConsumerThread(condition=condition, thread_name="consumer_thread_2")
    consumer_thread_3 = ConsumerThread(condition=condition, thread_name="consumer_thread_3")
    consumer_thread_4 = ConsumerThread(condition=condition, thread_name="consumer_thread_4")
    consumer_thread_5 = ConsumerThread(condition=condition, thread_name="consumer_thread_5")

    producer.start()
    consumer_thread_1.start()
    consumer_thread_2.start()
    consumer_thread_3.start()
    consumer_thread_4.start()
    consumer_thread_5.start()


if __name__ == "__main__":
    main()