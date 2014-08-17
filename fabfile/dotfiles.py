#!/usr/local/bin/python
# -*- codings:utf-8 -*-

import cuisine as cs
import fabric.api as fb
from fabric.contrib.files import exists
@fb.task
def setup() :
    if not exists('~/dotfiles') :
        cs.run('git clone https://github.com/yokotanaohiko/dotfiles.git')
    with cs.cd('~/dotfiles') :
        cs.run('setup.sh')
        cs.run('vim -c NeoBundleInstall -c q')
    
