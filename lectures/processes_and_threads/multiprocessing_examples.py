from multiprocessing import Process
import time


def fun():
    print('starting fun')
    time.sleep(2)
    print('finishing fun')


def main():
    p = Process(target=fun)
    p.start()
    p.join()


if __name__ == '__main__':
    print('starting main')
    main()
    print('finishing main')


from multiprocessing import Process
import time


def fun():
    print('calling fun')
    time.sleep(2)


def main():
    print('main fun')
    p = Process(target=fun)
    p.start()
    print(f'Process p is alive: {p.is_alive()}')
    p.join()



if __name__ == '__main__':
    main()

from multiprocessing import Process
import os


def fun():
    print('--------------------------')
    print('calling fun')
    print('parent process id:', os.getppid())
    print('process id:', os.getpid())


def main():
    print('main fun')
    print('process id:', os.getpid())
    p1 = Process(target=fun)
    p1.start()
    p1.join()
    p2 = Process(target=fun)
    p2.start()
    p2.join()


if __name__ == '__main__':
    main()

from multiprocessing import Process, current_process
import time


def worker():
    name = current_process().name
    print(name, 'Starting')
    time.sleep(2)
    print(name, 'Exiting')


def service():
    name = current_process().name
    print(name, 'Starting')
    time.sleep(3)
    print(name, 'Exiting')


if __name__ == '__main__':
    service = Process(name='Service 1', target=service)
    worker1 = Process(name='Worker 1', target=worker)
    worker2 = Process(target=worker)  # use default name
    worker1.start()
    worker2.start()
    service.start()

import time
from multiprocessing import Process


class Worker(Process):
    def run(self):
        print(f'In {self.name}')
        time.sleep(2)


def main():
    worker = Worker()
    worker.start()
    worker2 = Worker()
    worker2.start()
    worker.join()
    worker2.join()


if __name__ == '__main__':
    main()

import os

print(os.cpu_count())