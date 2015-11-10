#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import ConfigParser
import os
import shutil
import yaml


__version__ = '0.0.1'


parser = argparse.ArgumentParser()
parser.add_argument('user', nargs='?', default='default',
                    help='user setting you set')
parser.add_argument('-c', '--config-file', help='config file.')
args = parser.parse_args()

active_user = args.user
config_file = args.config_file

if config_file is None:
    config_file = os.path.expanduser('~/.multisettings.yaml')

config = yaml.load(open(config_file))

for usr, files in config.items():
    for default, specific in files.items():
        if os.path.exists(specific):
            continue
        if os.path.exists(default):
            yn = raw_input('Can I rename file {0} -> {1}? [y/n]: '.format(default, default + '.default'))
            if yn.lower() != 'y':
                continue
            shutil.move(default, default + '.default')
            os.symlink(default + '.default', specific)

config = ConfigParser.RawConfigParser()
config.add_section('core')
config.set('core', 'active_user', active_user)

dotfile = os.path.expanduser('~/.multisettings')
with open(dotfile, 'wb') as f:
    config.write(f)
