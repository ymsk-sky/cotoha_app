# -*- coding: utf-8 -*-

import requests
import json
import sys

BASE_URL = 'https://api.ce-cotoha.com/api/dev/'

def main():
    client_id, client_secret = get_client_info()
    print(client_id)
    print(client_secret)


def get_client_info():
    """クライアント情報を取得する
    params
    ----
    なし

    returns
    ----
    id_ : str
        Client ID
    secret : str
        Client secret
    """

    f = open('.client_info')
    id_ = f.readline().replace('\n', '').split(':')[1]
    secret = f.readline().replace('\n', '').split(':')[1]
    f.close()

    return id_, secret


if __name__ == '__main__':
    main()
