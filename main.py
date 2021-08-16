#
#coding by hdnkt
#
#ここ24時間で該当ワードが何回つぶやかれたか
#（RTを含んでしまうのでどうしよう）
#

import tweepy
import datetime

# 認証に必要なキーとトークン
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET =""

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# キーワードからツイートを取得
api = tweepy.API(auth)

#24時間前
yesterday = datetime.datetime.now()-datetime.timedelta(days=1)

def count_word_this1day(keyword):
    mid = 10**50
    count = 0
    while True:
        flag = False
        tweets = api.search(q=keyword,count=100,lang="ja",result_type="recent",max_id=mid)
        for tweet in tweets:
            if yesterday<tweet.created_at:
                count+=1
                mid = tweet.id -1
                print(tweet.text[0:30])
            else:
                flag=True
                break
        if flag:
            break
        if count > 10000:
            break

    print(count)

count_word_this1day("競技プロ")
