# import readline,rlcompleter
# readline.parse_and_bind("tab: complete")
import os
import re
import sys
import copy
import json
import pytz
import mock
import time
import uuid
import string
import random
import couchdb
import logging
import requests
import functools
import itertools
import simplejson
import collections

import urllib.parse
q = quote = urllib.parse.quote
u = uq = unquote = urllib.parse.unquote

import decimal
from decimal import Decimal
D = Decimal

import datetime
from datetime import datetime, timedelta

from pprint import pprint, pformat
pp = pprint

logging.getLogger().addHandler(logging.StreamHandler())
LOG = logger = logging.getLogger(__name__)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
LOG.addHandler(ch)

nicely = lambda x: print(simplejson.dumps(x, indent=4, sort_keys=True))
def nicely2(serializable_object):
    print(simplejson.dumps(serializable_object, indent=4, sort_keys=True))

def generate_string(length=10, source=string.ascii_lowercase):
    return ''.join(random.choice(source) for x in range(length))

gs = generate_string
gsp = functools.partial(generate_string, source=string.printable)


