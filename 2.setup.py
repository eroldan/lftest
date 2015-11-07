#!/bin/env python

import os.path
from shell import ex
from tool import *


class Run(Router):
    def set_max_fds(self):
        f = open('/etc/sysctl.d/max-fds.conf', 'w')
        f.truncate() 
        f.writelines(['fs.file-max = 399000\n'])
        f .close()

    def common(self):
        self.set_max_fds()
        assert ex('systemctl stop systemd-sysctl.service').re() == 0
        assert ex('systemctl start systemd-sysctl.service').re() == 0

    def Ubuntu(self):
        self.set_max_fds()
        assert ex('start procps').re() == 0
        
Run()
