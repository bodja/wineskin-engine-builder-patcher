from .base import BuildBase


class Autoreconf(BuildBase):

    def run(self):
        return self.shell.run('autoreconf -fvi')  # TODO: proper options
