AUTHOR = u"Kellan"
SITENAME = u"Noisebridge Learning Python"
SITEURL = 'http://www.pycourse.com'
RELATIVE_URLS = False

TIMEZONE = 'America/Los_Angeles'
ARTICLE_DIR = ('articles')
ARTICLE_EXCLUDES = ('pages')
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'service'
PATH = 'src/'
OUTPUT_PATH = 'output/'
STATIC_PATHS = ['images']
DISQUS_SITENAME = "pycourse"

SOCIAL = (('Liz\'s Site', 'http://www.eleddy.com'),
          ('Liz\'s Twitter', 'http://twitter.com/eleddy'),
          ('Kellan\'s Site', 'http://kellanjacobs.com'),
          ('Kellan\'s Twitter', 'http://twitter.com/kellanjacobs'),)


DEFAULT_PAGINATION = 10