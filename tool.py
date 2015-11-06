import sys, platform

class OSRouter:
    def __init__(self):
        plat = "".join(platform.linux_distribution()).replace(' ', '_')
        for n in range(len(plat)):
            p = plat[:-n]
            op = getattr(self, p, None)
            if op:
                #print 'Matched {0}'.format(p)
                return op()
        else: return self.default()


class Router(OSRouter):
    def default(self):
        print 'Don\'t know what to do, exiting'
        sys.exit(1)

    def common(self):
        print 'This is a nice LSB OS'

    def RedHat(self):
        self.common()
    CentOS = RedHat

    def Ubuntu(self):
        self.common()

    def OpenSuse(self):
        self.common()


def success():
    print 'Item passed'
    sys.exit(0)

def fail():
    print 'Item Failed'
    sys.exit(33)

if __name__ == '__main__':
    Router()


