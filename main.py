# -*- coding: utf-8 -*-

import requests
import json
import sys

BASE_URL = 'https://api.ce-cotoha.com/api/dev/'

def main():
    client_id, client_secret = get_client_info()
    access_token = auth(client_id=client_id,
                        client_secret=client_secret)

    document = """
               ルイズ！ルイズ！ルイズ！ルイズぅぅうううわぁああああああああああああああああああああああん！！！
               あぁああああ…ああ…あっあっー！あぁああああああ！！！ルイズルイズルイズぅううぁわぁああああ！！！
               あぁクンカクンカ！クンカクンカ！スーハースーハー！スーハースーハー！いい匂いだなぁ…くんくん
               んはぁっ！ルイズ・フランソワーズたんの桃色ブロンドの髪をクンカクンカしたいお！クンカクンカ！あぁあ！！
               間違えた！モフモフしたいお！モフモフ！モフモフ！髪髪モフモフ！カリカリモフモフ…きゅんきゅんきゅい！！
               小説12巻のルイズたんかわいかったよぅ！！あぁぁああ…あああ…あっあぁああああ！！ふぁぁあああんんっ！！
               アニメ2期放送されて良かったねルイズたん！あぁあああああ！かわいい！ルイズたん！かわいい！あっああぁああ！
               コミック2巻も発売されて嬉し…いやぁああああああ！！！にゃああああああああん！！ぎゃああああああああ！！
               ぐあああああああああああ！！！コミックなんて現実じゃない！！！！あ…小説もアニメもよく考えたら…
               ル イ ズ ち ゃ ん は 現実 じ ゃ な い？にゃあああああああああああああん！！うぁああああああああああ！！
               そんなぁああああああ！！いやぁぁぁあああああああああ！！はぁああああああん！！ハルケギニアぁああああ！！
               この！ちきしょー！やめてやる！！現実なんかやめ…て…え！？見…てる？表紙絵のルイズちゃんが僕を見てる？
               表紙絵のルイズちゃんが僕を見てるぞ！ルイズちゃんが僕を見てるぞ！挿絵のルイズちゃんが僕を見てるぞ！！
               アニメのルイズちゃんが僕に話しかけてるぞ！！！よかった…世の中まだまだ捨てたモンじゃないんだねっ！
               いやっほぉおおおおおおお！！！僕にはルイズちゃんがいる！！やったよケティ！！ひとりでできるもん！！！
               あ、コミックのルイズちゃああああああああああああああん！！いやぁあああああああああああああああ！！！！
               あっあんああっああんあアン様ぁあ！！シ、シエスター！！アンリエッタぁああああああ！！！タバサｧぁあああ！！
               ううっうぅうう！！俺の想いよルイズへ届け！！ハルケギニアのルイズへ届け！
               """.replace(' ', '').replace('！', '。')
    sent_len = 3
    result = call_api_summary(access_token=access_token,
                              document=document,
                              sent_len=sent_len)
    print(result['result'])


def call_api_user_attribute(access_token):
    pass


def call_api_summary(access_token, document, sent_len):
    """要約(β)
    文単位で重要度を算出しスコアを付与し要約文数に応じて重要文を返す

    params
    ----
    access_token : str
        access token
    document : str
        文章
    sent_len : int
        重要文の文数

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
        'document': document,
        'sent_len': sent_len
    }

    r = requests.post(BASE_URL + 'nlp/beta/summary',
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
