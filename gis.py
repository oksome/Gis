#!/usr/bin/env python

import sys
from os import system

argv = sys.argv[1:]

if argv == ['s']:
    system('git status')
else:
    system('Unknown command')
