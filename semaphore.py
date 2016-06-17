''' script to demonstrate the use ofsemaphore construct '''

import threading
import time
import random

# default value of Semaphore is 1 
phore = threading.Semaphore(0)

#consumer consumes item once the value is genrated by the producer by monitoring
# the semaphore value 
def consumer():
    print('consumer is waiting...')
    phore.acquire()
    print("consumer consumed item :%s"%item)

# producer produces items and changes the value of sempahore to notify the consumer
def producer():
    global item
    time.sleep(10)
    item = random.randint(0,1000)
    print("producer produced item: %s"%item)
    phore.release()

# driver area 
if __name__ == '__main__':
    for i in range (0,5):
        t = threading.Thread(target = producer)
        t2 = threading.Thread(target = consumer)
        t.start()
        t2.start()
        t.join()
        t2.join()
    print('program terminates')
