from .base import Formula


class LibPng(Formula):
    url = 'https://download.sourceforge.net/libpng/libpng-1.6.31.tar.xz'

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-dependency-tracking',
            '--disable-silent-rules',
        ]
