from .base import Formula


class Libtool(Formula):
    url = 'http://ftpmirror.gnu.org/libtool/libtool-2.4.6.tar.gz'

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-dependency-tracking',
            '--enable-ltdl-install',
        ]
