import os
import sys
import urllib.request
import tweepy

PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

# ROOT PATH
sys.path.append(PARENT_DIR)
from etc.config import *


def tweet_feed(product_items, status, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    name = product_items['name']
    link = product_items['link']
    image = product_items['image']
    size = product_items['size']
    price = product_items['price']

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweet = f"{status}: {name} [{size}] - {price}\n\n{link}"
    try:
        # saves image link in temp dir and return tuple object
        temp = urllib.request.urlretrieve(image)

        # file path is first in tuple
        jpg = temp[0]

        # upload image
        media = api.media_upload(jpg)

        # tweet
        status = api.update_status(status=tweet, media_ids=[media.media_id])
        if status == 200:
            log.info(f"NEW TWEET: {name} [{size}] {link}")
    except tweepy.Forbidden:
        log.error(f"Duplicate Tweet for {name}")
    except Exception as e:
        log.error(e)
