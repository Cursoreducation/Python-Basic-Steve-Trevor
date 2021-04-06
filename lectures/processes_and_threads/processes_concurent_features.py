from concurrent.futures import ProcessPoolExecutor
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

# Two processes

# With two processes we can do them both at once
start = time.time()
import os
with ProcessPoolExecutor(max_workers=(os.cpu_count() - 2)) as pool:
    pool.submit(calculation)
    pool.submit(calculation)

print(f'Two processes total time: {time.time() - start}\n\n')

# start = time.time()
# processes = Process(target=calculation)
# processes.start()
# enter_username()
# processes.join()  # waits fro the process to finish
#
# print(f'Two processes total time: {time.time() - start}\n\n')
