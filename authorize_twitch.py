import re

from utils.db import db
from utils.settings import TWITCH_CLIENT_ID

print("Please visit the following link:")
USER_AUTH_URL = 'https://api.twitch.tv/kraken/oauth2/authorize?' \
                'response_type=token&' \
                'client_id={}&' \
                'redirect_uri={}&' \
                'scope={}'.format(
    TWITCH_CLIENT_ID,
    'http://example.com/',
    'channel_feed_edit',
)
print(USER_AUTH_URL)

oauth_url = raw_input("Copypaste the url you have arrived at: ")

try:
    db.set(
        'twitch_access_token',
        re.findall(r'access_token=(\w+)', oauth_url)[0]
    )
    db.dump()
    print("Access granted, keys saved.")

except IndexError:
    raise BaseException("Unable to parse url, url format is incorrect.")

exit(0)
