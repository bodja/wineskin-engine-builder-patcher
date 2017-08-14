from .base import Formula


class Libquicktime(Formula):
    url = 'https://libquicktime.sourceforge.io/'

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-debug',
            '--disable-dependency-tracking',
            '--enable-gpl',
            '--without-doxygen',
            '--without-x',
            '--without-gtk',
        ]
