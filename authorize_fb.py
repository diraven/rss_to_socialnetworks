import facebook
import re
import requests
from utils.db import db
from utils.settings import FB_APP_ID, FB_SCOPE, FB_CLIENT_ID, FB_APP_SECRET

print "Please visit the following link:"
print "https://www.facebook.com/dialog/oauth?" \
      "client_id=%s&scope=%s&redirect_uri=https://www.facebook.com/connect/login_success.html" % (
          FB_APP_ID,
          FB_SCOPE,
      )

oauth_url = raw_input("Copypaste the url you have arrived at: ")

try:
    # Get code from FB
    print("Processing code...")
    code = re.findall(r'code=([^#]+)', oauth_url)[0]
    print("Done.")
except IndexError:
    raise BaseException("Unable to parse url, url format is incorrect.")

print("Getting FB access token...")
response = requests.get(
    "https://graph.facebook.com/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s" % (
        FB_CLIENT_ID,
        "https://www.facebook.com/connect/login_success.html",
        FB_APP_SECRET,
        code,
    ))
fb_access_token = re.findall(r'access_token=(\w+)', response.text)[0]

print("Getting page access token...")
graph = facebook.GraphAPI(fb_access_token, version='2.5')
result = graph.get_object('me/accounts')
print("Pages you have access to:")
for i, page in enumerate(result['data']):
    print("%d: %s" % (i, page['name']))

page_number = int(raw_input("Select page you want rss reposted to (input number): "))

db.set('fb_access_token', result['data'][page_number]['access_token'])
db.set('fb_page_id', result['data'][page_number]['id'])
db.dump()
print("Access granted, all keys saved.")
print("Done.")
