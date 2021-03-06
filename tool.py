import sys, platform

class CallRouter:
    def __init__(self):
        self.platform = "".join(platform.linux_distribution()).replace(' ', '_')
        for n in range(len(self.platform)):
            p = self.platform[:-n]
            op = getattr(self, p, None)
            if op:
                #print 'Matched {0}'.format(p)
                return op()
        else: return self.default()


class Router(CallRouter):
    def default(self):
        print 'Don\'t know what to do, exiting'
        sys.exit(100)

    def common(self):
        print 'This is a nice LSB OS'

    def RedHat(self):
        self.common()
    CentOS = RedHat

    def Ubuntu(self):
        self.common()

    def openSUSE(self):
        self.common()


def success():
    print 'Item passed'
    sys.exit(0)

def fail():
    print 'Item Failed'
    sys.exit(33)

if __name__ == '__main__':
    Router()


