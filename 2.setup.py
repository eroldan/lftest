#!/bin/env python

import os.path
from shell import ex
from tool import *


class Run(Router):
    def common(self):
        f = open('/etc/sysctl.d/max-fds.conf', 'w')
        f.truncate() 
        f.writelines(['fs.file-max = 199000'])
        f .close()

        assert ex('systemctl stop systemd-sysctl.service').re() == 0
        assert ex('systemctl start systemd-sysctl.service').re() == 0
Run()
