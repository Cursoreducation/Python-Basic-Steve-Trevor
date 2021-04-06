from threading import Thread
import time


def calculation():
    print('Starting the calculation')
    start = time.time()
    [x ** 2 for x in range(2000000)]
    print(f'Calculation time: {time.time() - start}')


def enter_username():
    username = input('Enter your name: ')
    start = time.time()
    greeting = f'Hello {username}'
    print(greeting)
    print(f'Enter username: {time.time() - start}')


start = time.time()
enter_username()
calculation()
print(f'Single thread total time: {time.time() - start}\n\n')

thread_1 = Thread(target=enter_username)
thread_2 = Thread(target=calculation)

start = time.time()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f'Two thread total time: {time.time() - start}\n\n')