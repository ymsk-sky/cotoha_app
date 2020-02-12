# -*- coding: utf-8 -*-

import requests
import json
import sys

BASE_URL = 'https://api.ce-cotoha.com/api/dev/'

def main():
    client_id, client_secret = get_client_info()
    access_token = auth(client_id=client_id,
                        client_secret=client_secret)


def auth(client_id, client_secret):
    token_url = 'https://api.ce-cotoha.com/v1/oauth/accesstokens'
    headers = {
        'Content-Type': 'application/json',
        'charset': 'UTF-8'
    }
    data = {
        'grantType': 'client_credentials',
        'clientId': client_id,
        'clientSecret': client_secret
    }

    r = requests.post(token_url,
                      headers=headers,
                      data=json.dumps(data))

    return r.json()['access_token']


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
