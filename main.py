from utils.post_twitch_feed import post_twitch_feed

__author__ = 'diraven'

import time

from dateutil import parser
import feedparser
from utils.settings import RSS_URL
from utils.db import db

last_post_datetime = None
try:
    last_post_datetime = parser.parse(db.get('last_post_datetime'))
except AttributeError:
    pass

feed = feedparser.parse(RSS_URL)
for entry in reversed(feed.entries):
    post_datetime = parser.parse(entry.published)
    if not last_post_datetime or last_post_datetime < post_datetime:
        post_vk(entry)
        # post_fb(entry)
        post_twitch_feed(entry)

        db.set('last_post_datetime', entry.published)
        db.dump()
        last_post_datetime = parser.parse(entry.published)
        time.sleep(10)

pass
