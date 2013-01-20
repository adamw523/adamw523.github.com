import feedparser
from hyde.plugin import Plugin

class AWRssFeedPlugin(Plugin):
    def __init__(self, site):
        super(AWRssFeedPlugin, self).__init__(site)
        self.site = site

    def begin_site(self):
        adamw523_feed = feedparser.parse('http://adamw523.posterous.com/rss.xml')
        with open('content/_adamw523_feed.html', 'w') as o:
            for e in adamw523_feed.entries:
                o.write('<li><a href="%s">%s</a></li>' % (e.link, e.title))

