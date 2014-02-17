#!/usr/bin/env python2

import sys
from os import system

argv = sys.argv[1:]

if argv == ['s']:
    system('git status')
else:
    system('Unknown command')
