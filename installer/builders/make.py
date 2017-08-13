from .base import BuildBase


class Make(BuildBase):

    def run(self):
        self.configure()
        self.make()
        self.install()

    def configure(self):
        return self.shell.run('./configure', *self.opts)

    def make(self):
        return self.shell.run('make')

    def install(self):
        return self.shell.run('make install')
