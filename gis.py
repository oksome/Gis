#!/usr/bin/env python

import sys
from os import system

argv = sys.argv[1:]

if argv == ['s']:
    system('git status')
elif argv == ['delete', 'last', 'commit']:
    # nuke last commit and never see it again
    system('git reset --hard HEAD~1')
elif argv == ['undo', 'last', 'commit']:
    # undo the commit but keep your changes for a bit of editing before you do a better commit
    system('git reset HEAD~1')
else:
    print('Unknown command')

