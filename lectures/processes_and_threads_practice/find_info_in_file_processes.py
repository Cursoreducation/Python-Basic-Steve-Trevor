import glob
import time
from concurrent.futures import ProcessPoolExecutor


def find_by_patter(filename, pattern):
    line_container = set()
    with open(filename) as f:
        for line in f:
            if pattern in line:
                line_container.add(line)
    return line_container


def find_all_by_pattern(directory_path, pattern):
    files = glob.glob(f'{directory_path}/*.py')
    container = set()
    with ProcessPoolExecutor() as pool:
        result = pool.map(find_by_patter, files, pattern)
        for res in result:
            container.update(res)
    return container


if __name__ == "__main__":
    start = time.time()
    search_by_patter = find_all_by_pattern('.', pattern='s')
    search_by_patter = find_all_by_pattern('.', pattern='i')
    search_by_patter = find_all_by_pattern('.', pattern=' ')
    end = time.time() - start
    print(f'Search time in {end} seconds')

    for line in search_by_patter:
        print(line)
