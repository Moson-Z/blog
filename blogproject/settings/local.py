#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
from .common import *

SECRET_KEY = 'development-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

HAYSTACK_CONNECTIONS['default']['URL'] = 'http://101.37.17.120:9200/'