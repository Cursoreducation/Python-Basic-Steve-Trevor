import requests
import time
from concurrent.futures import ThreadPoolExecutor
import threading

sites = ['https://www.google.com', 'https://uk.wikipedia.org', 'https://refactoring.guru/'] * 50

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f'Reading {len(response.content)} from {url}')


def download_all_sites(all_sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, all_sites)


if __name__ == "__main__":
    start = time.time()
    download_all_sites(sites)
    end_time = time.time() - start
    print(f'Downloaded {len(sites)} in {end_time} seconds')
