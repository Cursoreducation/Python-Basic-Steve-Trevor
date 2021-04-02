import sys
import getopt

def full_name():
    first_name = None
    last_name = None

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "l:f:")
    except:
        print('The arguments are missing')

    for opt, arg in opts:
        if opt in ['-f']:
            first_name = arg
        elif opt in ['-l']:
            last_name = arg
        else:
            other = arg
            print(other)
    print(f'{first_name} {last_name}')

full_name()