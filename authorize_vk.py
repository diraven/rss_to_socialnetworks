import re
from utils.db import db
from utils.settings import VK_CLIENT_ID, VK_SCOPE, VK_API_VERSION

print("Please visit the following link:")
print("https://oauth.vk.com/authorize?" \
      "client_id=%s&" \
      "scope=%s&" \
      "redirect_uri=https://oauth.vk.com/blank.html&" \
      "display=page&" \
      "v=%s&" \
      "response_type=token" % (
          VK_CLIENT_ID,
          VK_SCOPE,
          VK_API_VERSION,
      ))

oauth_url = input("Copypaste the url you have arrived at: ")

try:
    db.set('vk_access_token', re.findall(r'access_token=(\w+)', oauth_url)[0])
    db.set('vk_user_id', re.findall(r'user_id=(\d+)', oauth_url)[0])
    db.dump()
    print("Access granted, keys saved.")

except IndexError:
    raise BaseException("Unable to parse url, url format is incorrect.")

page_id = input("Input the Page ID you want to post to: ")
db.set('vk_page_id', int(page_id))
db.dump()
print("Page ID saved.")
