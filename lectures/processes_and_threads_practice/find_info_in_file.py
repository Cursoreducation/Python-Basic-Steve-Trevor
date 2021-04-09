"""
The script should find the line that you provided
in the provided directory
"""
import glob
import time


def find_by_patter(filename, pattern):
    line_container = set()
    with open(filename) as f:
        for line in f:
            if pattern in line:
                line_container.add(line)
    return line_container


def find_all_files(directory_path, pattern):
    files = glob.glob(f'{directory_path}/*.py')
    container = set()
    for file in files:
        result = find_by_patter(file, pattern)
        container.update(result)
    return container


if __name__ == '__main__':
    start = time.time()
    search_by_patter = find_all_files('.', pattern='s')
    search_by_patter = find_all_files('.', pattern='i')
    search_by_patter = find_all_files('.', pattern=' ')
    end = time.time() - start
    print(f'Search time in {end} seconds')
    for line in search_by_patter:
        print(line)
