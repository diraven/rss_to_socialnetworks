__author__ = 'diraven'

import time

from dateutil import parser
import feedparser
from utils.db import db
from utils.post_vk import post_vk

last_post_datetime = None
try:
    last_post_datetime = parser.parse(db.get('last_post_datetime'))
except AttributeError:
    pass

feed = feedparser.parse("http://mmomoc.pl/rss/")
for entry in reversed(feed.entries):
    post_datetime = parser.parse(entry.published)
    if not last_post_datetime or last_post_datetime < post_datetime:
        time.sleep(10)
        post_vk(entry)

        db.set('last_post_datetime', entry.published)
        db.dump()
        last_post_datetime = parser.parse(entry.published)

pass
