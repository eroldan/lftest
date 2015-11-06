#!/bin/env python
# Story:
# Using the sysctl tool, set the system wide file descriptor limit to 131070 and ensure that the value is applied on boot.

from shell import ex, pipe_all
from tool import *


class Run(Router):
    def common(self):

        out = pipe_all(['sysctl -a', 'grep "fs\.file-max =.*"']).stdout()
        for l in out.splitlines():
            k, v = l.strip().split(' = ')
        if v != '131070':
            fail()
        else: success()

Run()
