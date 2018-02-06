#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Panos Louridas'
SITENAME = 'Real World Algorithms Web Companion'
SITEURL = 'https://louridas.github.io/rwa'

PATH = 'content'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = [ './pelican-plugins' ]
PLUGINS = [ 'pelican-pcite', 'render_math' ]

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "themes/rwa"

STATIC_PATHS = ['assignments', 'images', 'notebooks', 'pdfs']

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

GOOGLE_ANALYTICS = "UA-103703286-1"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
