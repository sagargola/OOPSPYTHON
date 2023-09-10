'''In this programming I am trying to explain how multithreading works so that the program can run in parallel
we will use threading. We need to import threading and time. Here I m using a simple func which run and sleep after 1
sec while by default its one thread we are creating another thread and will the no of threads also and this new
thread will run when the main thread is sleeping on time.sleep'''

import threading
import time

def func():
    print("run")
    time.sleep(1)
    print("done")

x = threading.Thread(target = func) #creating a new thread
x.start() #start the thread
print(threading.active_count()) #will print 2 as we created on thread above