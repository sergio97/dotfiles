# import readline,rlcompleter
# readline.parse_and_bind("tab: complete")
import os
import re
import sys
import json
import mock
import uuid
import bleach
import random
import string
import couchdb
import decimal
import logging
import requests
import functools
import itertools
from pprint import pprint
from decimal import Decimal
from datetime import datetime, timedelta

pp = pprint
D = Decimal

logging.getLogger().addHandler(logging.StreamHandler())
LOG = logger = logging.getLogger(__name__)

def nicely(serializable_object):
    print(json.dumps(serializable_object, indent=4))

