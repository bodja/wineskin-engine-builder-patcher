from .base import Formula


class Libogg(Formula):
    url = 'https://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.gz'

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-dependency-tracking',
        ]
