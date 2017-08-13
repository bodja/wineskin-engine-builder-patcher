from utils.shell import Shell


class BuildBase(object):

    def __init__(self, src, opts, env):
        self.src = src
        self.opts = opts
        self.env = env
        self.shell = Shell(self.src, self.env)

    def run(self):
        raise NotImplementedError
