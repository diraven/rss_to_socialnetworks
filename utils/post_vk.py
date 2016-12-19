from io import BytesIO

import requests
from utils.db import db
from utils.html2text_processor import html2text_processor
import vk

vk_access_token = db.get('vk_access_token')
if not vk_access_token:
    raise Exception('VK Access Token not found. Run authorize_vk.py first.')
session = vk.Session(vk_access_token)
api_vk = vk.API(session)


def post_vk(rss_entry):
    # photo_upload_url = api_vk.photos.getWallUploadServer()['upload_url']

    attachments = []
    # for url in [link.href for link in rss_entry.links if 'image' in link.type]:
    #     image = BytesIO(requests.get(url).content)
    #     r = requests.post(
    #         photo_upload_url,
    #         files={
    #             'photo': ('image.jpg', image)
    #         },
    #     )
    #     upload_result = api_vk.photos.saveWallPhoto(
    #         photo=r.json()['photo'],
    #         server=r.json()['server'],
    #         hash=r.json()['hash']
    #     )
    #     attachments.append(upload_result[0]['id'])
    attachments.append(rss_entry.link)

    api_vk.wall.post(
        owner_id=-db.get('vk_page_id'),
        from_group=1,
        message=u"{title}\r\n\r\n"
                u"{message}".format(title=rss_entry.title, message=html2text_processor.handle(rss_entry.summary)),
        attachments=','.join(attachments)
    )
