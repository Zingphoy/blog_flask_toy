# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.logger
~~~~~~~~~~~~~~~

"""

import os
import sys
from loguru import logger

# set up logger
log_format = '<green>{time}</green> [{level}]<level>{message}</level>'
top = os.path.dirname
log_file = top(top(__file__)) + '/blog.log'
logger.add(log_file, format=log_format, rotation='10 MB', retention='3 days')
logger.add(sys.stdout, colorize=True, format=log_format)
