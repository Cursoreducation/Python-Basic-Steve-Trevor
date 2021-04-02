from sys import argv

print(f'This is the name of the script: {argv[0]}')
print(f'Arguments list: {str(argv)}')
print(f'Number of the elements including the name of the script: {len(argv)}')
print(f'Number of the elements without the name of the script: {len(argv) - 1}')

print(argv[1])
print(argv[2])
print(argv[1:])

add = 0.0

n = len(argv)

for i in range(1, n):
    add += float(argv[i])

print(f'The sum is {add}')


try:
    arg = argv[2]
except IndexError:
    raise SystemExit(f'The argument you trying to get is missing. Arguments list: {argv}')