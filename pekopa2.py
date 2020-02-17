# -*- coding: utf-8 -*-

import requests
import json
import sys

BASE_URL = 'https://api.ce-cotoha.com/api/dev/'

def main():
    client_id, client_secret = get_client_info()
    access_token = auth(client_id=client_id,
                        client_secret=client_secret)

    sentences = ['そまたせしました',  # お待たせしました
                 'フォレの名前は松陰寺太勇', # 俺の名前は
                 'タクシーフン転手',]  # タクシー運転手

    responses = [call_api_detect_misrecognition(access_token=access_token, sentence=s) for s in sentences]

    for r in responses:
        result = r['result']
        print(result)


def call_api_detect_misrecognition(access_token, sentence):
    """音声認識誤り検知（β）
    音声認識処理後のテキストから認識誤りっぽいところを訂正する。

    params
    ----
    access_token : str
        access token
    sentence : str
        文章

    returns
    ----
    json_data : json
    """

    headers = {
        'Content-Type': 'application/json',
        'charset': 'UTF-8',
        'Authorization': 'Bearer {0}'.format(access_token)
    }
    data = {
        'sentence': sentence
    }

    r = requests.post(BASE_URL + 'nlp/beta/detect_misrecognition',
                      headers=headers,
                      data=json.dumps(data))
    json_data = r.json()

    return json_data


def auth(client_id, client_secret):
    """アクセストークンを取得する. 24時間有効らしい（未検証）
    params
    ----
    client_id : str
        Client ID
    client_secret : str
        Client secret

    returns
    ----
    access_token
        access token
    """

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
    access_token = r.json()['access_token']

    return access_token


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
