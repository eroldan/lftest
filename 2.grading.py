#!/bin/env python
# Story:
# Using the sysctl tool, set the system wide file descriptor limit to 131070 and ensure that the value is applied on boot.

from shell import ex, pipe_all
from tool import *


class Run(Router):
    def check(self):

        if self.platform.startswith('Ubuntu'): sysctl = '/sbin/sysctl'
        else: sysctl = '/usr/sbin/sysctl'

        out = pipe_all(['{} -a'.format(sysctl), 'grep "fs\.file-max =.*"']).stdout()
        for l in out.splitlines():
            k, v = l.strip().split(' = ')
        if v != '131070':
            fail()
        else: success()


    def common(self):
        assert ex('systemctl stop systemd-sysctl.service').re() == 0
        assert ex('systemctl start systemd-sysctl.service').re() == 0
        self.check()


    def Ubuntu(self):
        assert ex('start procps').re() == 0
        self.check()

Run()
