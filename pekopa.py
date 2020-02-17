# -*- coding: utf-8 -*-

import requests
import json
import sys

BASE_URL = 'https://api.ce-cotoha.com/api/dev/'

def main():
    client_id, client_secret = get_client_info()
    access_token = auth(client_id=client_id,
                        client_secret=client_secret)

    sentences = ['どこ見て運転してんだよって言えてる時点で無事でよかった。そうだろ？無事であることが何より大切なんだ。',
                 '2回もぶつかるってことは俺が車道側に立っていたのかもしれない。もう誰かのせいにするのはやめにしよう。',
                 'いやブーンじゃなくてスーンの車がもう街中に溢れてる。',
                 'いや知らねーんだったら教えてあげよう。そうだろ？知識は水だ。独占してはいけない。',
                 'いや右だっつってんのに何で3回も左に曲がると右になってる。すごいよ運転手さん。',
                 'いや俺がナビしてた時間返せよって言って実際に時間が返ってきたよーって人。いないだろ？できないことを求めるのもやめにしよう。',
                 'いや休憩は取ろう。働き方を変えていこう。',
                 'いやハンドルを握らなくていい時代がもう目の前まで来てる。',
                 'いやナスじゃねぇとは言い切れない色合いだ。ヘタも付いている。',
                 'いやキャラ芸人になるしかなかったんだ。何かが欲しかった。',
                 'いやさっき取った休憩は短かった。そうだろ？日本人は真面目で勤勉だけど、休憩を取らなさすぎだ。だから他の先進国に比べて労働生産性が低いんじゃないのか。働き方改革って法律でどうこうできる問題なのか？なぁお前はどう思う？',
                 'お前よりはうるさい。',
                 '急に正面が変わったのか？',
                 'いや戻り方は人それぞれだ。',
                 'いやいい加減なことなんてない。',
                 'しょうもねぇボケやってんじゃねえよって言ってる俺もしょうもない人間だ。']

    responses = [call_api_sentiment(access_token=access_token, sentence=s) for s in sentences]

    for r in responses:
        result = r['result']
        sentiment = result['sentiment']  # 感情
        score = result['score']  # スコア

        print(result)
        # print(sentiment, score)


def call_api_sentiment(access_token, sentence):
    """感情分析
    テキストから感情を判定する

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

    r = requests.post(BASE_URL + 'nlp/v1/sentiment',
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
