import threading


global_data = threading.local()


def show():
    print threading.current_thread().getName(), global_data.num


def thread_cal():
    global_data.num = 0
    for _ in xrange(1000):
        global_data.num += 1
    show()

threads = []
for i in range(10):
    threads.append(threading.Thread(target=thread_cal))
    threads[i].start()

print "Main thread: ", global_data.__dict__
