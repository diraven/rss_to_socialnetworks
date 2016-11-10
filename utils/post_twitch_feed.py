import requests

from utils.db import db
from utils.html2text_processor import html2text_processor

twitch_access_token = db.get('twitch_access_token')
if not twitch_access_token:
    raise Exception(
        'Twitch Access Token not found. Run authorize_twitch.py first.'
    )


def post_twitch_feed(rss_entry):
    response = requests.post(
        'https://api.twitch.tv/kraken/feed/diraven/posts?oauth_token={}'.format(
            twitch_access_token
        ),
        headers={
            'Accept': 'application/vnd.twitchtv.v3+json',
        },
        data={"content": u"{}\n{}\n{}".format(
            rss_entry.title,
            rss_entry.link,
            html2text_processor.handle(rss_entry.summary),
        )}
    )

    print(response.text)
