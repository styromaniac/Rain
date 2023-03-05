#!/usr/bin/env python3

import os
import re
import urllib.parse
import urllib.request
import sys
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import hashlib

class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag in ['a', 'link']:
            href = self.get_attr(attrs, 'href')
            if href is not None:
                self.add_link(href)
        elif tag in ['script', 'img', 'video', 'audio']:
            src = self.get_attr(attrs, 'src')
            if src is not None:
                self.add_link(src)

    def add_link(self, link):
        url = urllib.parse.urljoin(self.base_url, link)
        self.links.append(url)

    def get_attr(self, attrs, attr_name):
        for attr in attrs:
            if attr[0].lower() == attr_name:
                return attr[1]

def download_website(source, dest):
    # Download sourcechecksums.txt
    checksum_url = urllib.parse.urljoin(source, 'sourcechecksums.txt')
    try:
        checksum_file = download_url(checksum_url, binary=True)
        with open(os.path.join(dest, 'sourcechecksums.txt'), 'wb') as f:
            f.write(checksum_file)
    except Exception as e:
        print(f'Error downloading {checksum_url}: {e}')
        return

    # Check sha256sums of local copies against those in sourcechecksums.txt
    with open(os.path.join(dest, 'sourcechecksums.txt'), 'r') as f:
        checksums = f.readlines()

    for checksum in checksums:
        if checksum.startswith('#') or len(checksum.strip()) == 0:
            continue

        file_path, sha256sum = checksum.split()
        local_path = os.path.join(dest, file_path)

        if not os.path.exists(local_path):
            print(f'Downloading {file_path}...')
            download_url_to_file_v2(urllib.parse.urljoin(source, file_path), source, dest)
        else:
            with open(local_path, 'rb') as f:
                content = f.read()
                hash_object = hashlib.sha256(content)
                hex_dig = hash_object.hexdigest()
                if hex_dig == sha256sum:
                    print(f'{file_path} already up-to-date.')
                else:
                    print(f'Updating {file_path}...')
                    download_url_to_file_v2(urllib.parse.urljoin(source, file_path), source, dest)

    # Download website
    try:
        html = download_url(source)
    except Exception as e:
        print(f'Error downloading {source}: {e}')
        return

    parser = LinkParser(source)
    parser.feed(html)
    urls = parser.links

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = []
        for url in urls:
            if source not in url:
                continue

            future = executor.submit(download_url_to_file_v2, url, source, dest)
            futures.append(future)

        for future in futures:
            try:
                result = future.result()
            except Exception as e:
                print(f'Error downloading {future}: {e}')

    # Save index.html
    dest_path = os.path.join(dest, 'index.html')
    with open(dest_path, 'w') as f:
        f.write(html)

    # Update links in index.html
    index_links = [url.replace(source, '') for url in urls if source in url]
    update_links_in_file(dest_path, index_links)

def download_url_to_file_v2(url, source, dest):
    try:
        content = download_url(url, binary=True)
    except Exception as e:
        print(f'Error downloading {url}: {e}')
        return

    path = url.replace(source, '')

    if path == '':
        path = 'index.html'

    dest_path = os.path.join(dest, path.lstrip('/'))
    dir_path = os.path.dirname(dest_path)

    os.makedirs(dir_path, exist_ok=True)

    try:
        with open(dest_path, 'wb') as f:
            f.write(content)
    except Exception as e:
        print(f'Error writing file {dest_path}: {e}')
        return

def download_url(url, binary=False):
    with urllib.request.urlopen(url) as response:
        if binary:
            return response.read()
        else:
            return response.read().decode('utf-8')

def update_links_in_file(file_path, links):
    with open(file_path, 'r') as f:
        content = f.read()

    for link in links:
        relative_path = os.path.relpath(link, os.path.dirname(file_path))
        content = content.replace(link, relative_path)

    with open(file_path, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: rain <dest> <source>')
        sys.exit(1)

    dest, source = sys.argv[1], sys.argv[2]
    download_website(source, dest)