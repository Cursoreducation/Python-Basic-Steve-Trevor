"""
Downloading content over the network.
You need to download web pages from a few sites,
but it really could be any network traffic.
"""
import requests
import time

sites = ['https://www.google.com', 'https://uk.wikipedia.org', 'https://refactoring.guru/'] * 50


# result = requests.get(sites[0])
# print(result)
def download_site(url, session):
    with session.get(url) as response:
        print(f'Reading {len(response.content)} from {url}')


def download_all_sites(all_sites):
    with requests.Session() as session:
        for site in all_sites:
            download_site(site, session)


if __name__ == '__main__':
    start = time.time()
    download_all_sites(sites)
    end_time = time.time() - start
    print(f'Downloaded {len(sites)} in {end_time} seconds')
