from threading import current_thread
import threading

thread_local = threading.local()


def hi():
    initialized = getattr(thread_local, 'initialized', None)
    if initialized is None:
        print('Nice to meet you', current_thread().name)
        thread_local.initialized = True
    else:
        print('Welcome back', current_thread().name)


# hi()
# hi()


def wont_work():
    thread_local = threading.local()
    initialized = getattr(thread_local, 'initialized', None)
    if initialized is None:
        print('Nice to meet you', current_thread().name)
        thread_local.initialized = True
    else:
        print('Welcome back', current_thread().name)

wont_work()
wont_work()
