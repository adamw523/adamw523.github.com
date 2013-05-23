import feedparser
from bs4 import BeautifulSoup
import requests
from hyde.plugin import Plugin
# from hyde.util import getLoggerWithNullHandler  
# logger = getLoggerWithNullHandler('hyde.engine')

class AWRssFeedPlugin(Plugin):
    def __init__(self, site):
        super(AWRssFeedPlugin, self).__init__(site)
        self.site = site

    def begin_site(self):
        self.logger.info("Fetching adamw523 blog RSS")

        feed_req = requests.get('http://blog.adamw523.com/feed/')
        soup = BeautifulSoup(feed_req.text)

        with open('content/_adamw523_feed.html', 'w') as o:
            for item in soup.find_all('item'):
                # self.logger.info(' '.join(['item', str(item.link), str(item.title)]))
                o.write('<li><a href="%s">%s</a></li>' % (item.link.text.encode('utf-8'), item.title.text.encode('utf-8')))

