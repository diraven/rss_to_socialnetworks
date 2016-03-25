# rss_to_socialnetworks
A very simple script to udate your VK and FB (coming later) groups/walls with news taken from RSS

## Notes
- Make sure to properly secure your utils/settings.py file and your data.db file as they both contain sensitive info.

## Installation:
- # cd to/your/cloned/project/dir
- # pip install virtualenv
- # virtualenv venv
- # source venv/bin/activate
- # pip install -r requirements.txt
- # cd utils
- # cp settings_example.py settings.py
- # vi settings.py
- # cd ..
- # python authorize_vk.py
- setup crontab record for "# python main.py" and let it run 