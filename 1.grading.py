#!/bin/env python

from tool import *
import pwd

pw_shell_idx = 6

class Run(Router):

    def common(self):
        try:
            u = pwd.getpwnam('projectmanager')
            if u[pw_shell_idx] != '/bin/bash': fail()

        except KeyError:
            fail()

        else:
            success()
Run()

