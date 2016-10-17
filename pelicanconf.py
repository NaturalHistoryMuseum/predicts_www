#!/usr/bin/env python3
from __future__ import unicode_literals

AUTHOR = 'Trustees of the Natural History Museum, London'
SITENAME = 'PREDICTS'

SITEURL = 'http://www.predicts.org.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CC_LICENSE = 'CC-BY'

# Blogroll
LINKS = (
    # ('SYNTHESYS', 'http://www.synthesys.info/'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/NaturalHistoryMuseum/predicts_www/'),
)

MENUITEMS = (
    ('Background', '{siteurl}/pages/background.html'.format(siteurl=SITEURL)),
    ('The science', '{siteurl}/pages/the-science.html'.format(siteurl=SITEURL)),
    ('Policy', '{siteurl}/pages/policy.html'.format(siteurl=SITEURL)),
    ('Contribute', '{siteurl}/pages/contribute.html'.format(siteurl=SITEURL)),
    ('Team', '{siteurl}/pages/team.html'.format(siteurl=SITEURL)),
    ('News', '{siteurl}/category/news.html'.format(siteurl=SITEURL)),
    ('Outputs', '{siteurl}/pages/outputs.html'.format(siteurl=SITEURL)),
    ('Earthworm Watch', '{siteurl}/pages/earthworm-watch.html'.format(siteurl=SITEURL)),
    ('Newsletter', '{siteurl}/pages/newsletter.html'.format(siteurl=SITEURL)),
)

DEFAULT_PAGINATION = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

GITHUB_URL = "https://github.com/NaturalHistoryMuseum/predicts_www"

THEME = "../pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'

CUSTOM_CSS = 'predicts.css'

STATIC_PATHS = ['images', 'predicts.css', 'newsletters']

FAVICON = 'images/predicts.ico'
SITELOGO = 'images/predicts120.png'
SITELOGO_SIZE = 95
HIDE_SITENAME = True

PYGMENTS_STYLE = 'friendly'

SHOW_COPYRIGHT = False
CC_ATTR_MARKUP = True
