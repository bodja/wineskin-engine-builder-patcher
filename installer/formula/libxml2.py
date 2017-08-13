from .base import Formula


class Libxml2(Formula):
    url = 'http://xmlsoft.org/sources/libxml2-2.9.4.tar.gz'

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-dependency-tracking',
            '--without-python',
            '--without-lzma',
        ]
