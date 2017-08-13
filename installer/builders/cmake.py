from .base import BuildBase


class CMake(BuildBase):

    def run(self):
        self.configure()
        self.make()
        self.install()

    def configure(self):
        return self.shell.run('cmake', *self.opts)

    def make(self):
        return self.shell.run('make')

    def install(self):
        return self.shell.run('make install')
