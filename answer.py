#!/bin/env python

from shell import ex
from tool import *


class Run(Router):
    def common(self):
        assert ex('usermod --shell /bin/bash projectmanager')

Run()
