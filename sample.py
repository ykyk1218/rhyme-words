import env

import sys
# Tweepyライブラリをインポート 
import tweepy 
# mongodb
from pymongo import MongoClient
from urllib.parse import urlparse
from pprint import pprint 

# 各種キーをセット
auth = tweepy.OAuthHandler(env.TWITTER_CONSUMER_KEY, env.TWITTER_CONSUMER_SECRET)
auth.set_access_token(env.TWITTER_ACCESS_TOKEN, env.TWITTER_ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# これだけで、Twitter APIをPythonから操作するための準備は完了。
print('Done!')

timeline = api.home_timeline()[0].text


if __name__ == "__main__":
  mongo_client = MongoClient(MONGO_URL)
  db_connect = mongo_client["rhyme-words"]
  db_connect.sample.insert_one({'tweet':timeline})

