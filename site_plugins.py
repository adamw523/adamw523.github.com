import feedparser
from hyde.plugin import Plugin
from hyde.util import getLoggerWithNullHandler  
logger = getLoggerWithNullHandler('hyde.engine')

class AWRssFeedPlugin(Plugin):
    def __init__(self, site):
        super(AWRssFeedPlugin, self).__init__(site)
        self.site = site

    def begin_site(self):
        logger.info("Fetching adamw523 blog RSS")
        adamw523_feed = feedparser.parse('http://blog.adamw523.com/rss.xml')
        with open('content/_adamw523_feed.html', 'w') as o:
            for e in adamw523_feed.entries:
                o.write('<li><a href="%s">%s</a></li>' % (e.link, e.title))

