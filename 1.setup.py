#!/bin/env python
# Story:
# Alter the projectmanager user account changing its default login shell from /bin/false to /bin/bash.

from shell import ex
from tool import *


class Run(Router):
    def common(self):
        ex('useradd projectmanager')
        assert ex('usermod --shell /bin/false projectmanager').re() == 0

Run()
