#!/bin/env python
# Story:
# Using the sysctl tool, set the system wide file descriptor limit to 131070 and ensure that the value is applied on boot.

from shell import ex
from tool import *

class Run(Router):
    def common(self):

        f = open('/etc/sysctl.d/max-fds.conf', 'w')
        f.truncate()
        f.writelines(['fs.file-max = 131070'])
        f .close()

        assert ex('sysctl --system')

Run()
