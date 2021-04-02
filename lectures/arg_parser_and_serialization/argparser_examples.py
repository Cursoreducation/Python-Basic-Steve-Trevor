import argparse

parser = argparse.ArgumentParser(description='Cursor lecture')

parser.add_argument('-n', '--name', default='Sio', help='To define the name of contributor')
parser.add_argument('--number', action='store_const', const=10, help='Should be int')
parser.add_argument('--is_required', action='store_true')
parser.add_argument('--custom', action='help')
parser.add_argument('--version', action='version', version='2.0')


parser.add_argument('-edu', '--education', choices=["highschool", "college", "university", 'pastgraduate', 'other'], required=True, type=str, help='You should choose one from this list')
args = parser.parse_args()

name = args.name
number = args.number
is_required = args.is_required
version = args.version
ed = args.education

if ed == 'college' or ed == 'university':
    print('Has degree')
elif ed == "highschool":
    print('Finished HighSchool')
elif ed == "pastgraduate":
    print('Working on it')
else:
    print("Doesn't have degree!")

if is_required:
    print(number)
else:
    print('No')

print(name)
print(number)
