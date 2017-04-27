# import readline,rlcompleter
# readline.parse_and_bind("tab: complete")
import os
import re
import sys
import json
import mock
import uuid
import string
import bleach
import random
import couchdb
import logging
import datetime
import requests
import functools
import itertools
from pprint import pprint
import decimal
from decimal import Decimal

pp = pprint
D = Decimal

logging.getLogger().addHandler(logging.StreamHandler())
LOG = logger = logging.getLogger(__name__)

def nicely(serializable_object):
    print(json.dumps(serializable_object, indent=4))

