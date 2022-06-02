'''
Author: dmdhrumilmistry
Project: github.com/dmdhrumilmistry/GooglePhish
Module: cloner.py
Description: clone webpage
Usage: python cloner.py -u https://google.com/ -n google.html
'''

import argparse
import os
import requests


def clone_page(url: str, page_name: str, save_dir: str) -> bool:
    file_path = os.path.join(save_dir, page_name)

    # create dir if doesn't exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # create session and make request to server
    session = requests.session()
    response = session.get(url)

    # if response is OK then store data
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return True

    return False


if __name__ == '__main__':
    # create argument parser obj
    parser = argparse.ArgumentParser(prog='cloner')

    # add args
    parser.add_argument(
        '-u', '--url', dest='url', help='URL of webpage which will be cloned', type=str, required=True)
    parser.add_argument('-n', '--name', dest='page_name',
                        help='save file name', type=str, required=True)
    parser.add_argument('-d', '--directory', dest='save_dir',
                        help='directory where file will be saved', default=os.path.join(os.getcwd(), 'cloned'))

    # parse args
    args = parser.parse_args()

    # get parsed arguments
    url = args.url
    page_name = args.page_name
    save_dir = args.save_dir

    # clone page
    if clone_page(url=url, page_name=page_name, save_dir=save_dir):
        print(f'[*] {url} webpage cloned successfully stored in {save_dir}')
    else:
        print(f'[!] Failed to clone {url} webpage')
