#!/usr/bin/env python3
import os
import yaml
import re

from getpass import getpass

cache = {}

def setup_cache():
    global cache

    cache_file = os.path.expanduser('~/.jirautils')

    if not os.path.isfile(cache_file):
        cache['server'] = input('server: ')
        cache['username'] = input('username: ')
        cache['password'] = getpass('password: ')

        # If the server does not start with http*:// enforce https as default
        if bool(re.match(r'^(http|https)://', cache['server'])) == False:
            cache['server'] = 'https://{}'.format(cache['server'])

        with open(cache_file, 'w') as f:
            f.write(yaml.dump(cache))
    else:
        with open(cache_file, 'r') as f:
            cache = yaml.load(f)

setup_cache()
