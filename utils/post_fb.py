import facebook

from utils.db import db
from utils.html2text_processor import html2text_processor

fb_access_token = db.get('fb_access_token')
if not fb_access_token:
    raise Exception('FB Access Token not found. Run authorize_fb.py first.')

fb_page_id = db.get('fb_page_id')
if not fb_page_id:
    raise Exception('FB Page ID not found. Run authorize_fb.py first.')

graph = facebook.GraphAPI(fb_access_token, version='2.5')


def post_fb(rss_entry):
    image = None
    for url in [link.href for link in rss_entry.links if 'image' in link.type]:
        image = url
        break

    result = graph.put_object(
        fb_page_id, 'feed',
        message=html2text_processor.handle(rss_entry.summary),
        link=rss_entry.link,
        picture=image,
    )

    pass
