import requests
import time
import multiprocessing
from multiprocessing import Pool

sites = ['https://www.google.com', 'https://uk.wikipedia.org', 'https://refactoring.guru/'] * 50

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        print(f'{multiprocessing.current_process().name}:Reading {len(response.content)} from {url}')


def download_all_sites(all_sites):
    with Pool(5, initializer=set_global_session) as pool:
        pool.map(download_site, all_sites)


if __name__ == '__main__':
    start = time.time()
    download_all_sites(sites)
    end = time.time() - start
    print(f'Downloaded {len(sites)} in {end} seconds')
