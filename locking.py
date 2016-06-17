''' Script to show the use of lock method to provide concurrency on a variable '''

#import threading module required for threading 
import threading

#global variables 
with_lock = 0 # value which will be operated under lock .
without_lock = 0 # value which will be operated without lock 
count = 10000 # variable to iterate 
locking = threading.Lock()#lock with two methods (quire and release)

def increment_with():
    global with_lock #to remove local and global context 
    for i in range(count):
        locking.acquire() #acquire lock
        with_lock +=1 #increment value by one
        locking.release()#release lock


def decrement_with():
    global with_lock #to remove local and global context
    for i in range(count):
        locking.acquire()#acquire lock 
        with_lock -=1#decrementvalue by one 
        locking.release()#release lock



def increment_without():
    # no locking used whatsoever 
    global without_lock
    for i in range(count):
        without_lock +=1

        

def decrement_without():
    # no locking here as well 
    global without_lock
    for i in range(count):
        without_lock -=1


# program driver section 
if __name__ == '__main__':
    # create threads
    t1 = threading.Thread(target = increment_with )
    t2 = threading.Thread(target = decrement_with )
    t3 = threading.Thread(target = increment_without )
    t4 = threading.Thread(target = decrement_without )
    #start threads 
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # main thread waits untill all threads complete their work 
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    # value after processing 
    print('without lock value :%d'%without_lock)
    print('with lock value:%d'%with_lock)
                
