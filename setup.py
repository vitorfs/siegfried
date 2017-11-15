# -*- coding: utf-8 -*-

import os
from setuptools import setup

APP = ['main.py']
DATA_FILES = ['staticfiles', 'db.sqlite3', ]
OPTIONS = {'argv_emulation': False,
           'strip': True,
           'iconfile': './siegfried.icns',
           'packages': ['siegfried', 'cheroot', 'cherrypy', 'django', 'django_crispy_forms', 'jaraco.classes', 'nltk', 'portend', 'pytz', 'six', 'tempora', 'xlrd', ],
           'plist': {
               'CFBundleIdentifier': 'com.vitorfs.siegfried',
               'CFBundleName': 'Siegfried',
               'CFBundleVersion': '1001',
               'CFBundleShortVersionString': '1.0',
               'NSHumanReadableCopyright': 'Copyright 2017 Vitor Freitas'}
           }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)