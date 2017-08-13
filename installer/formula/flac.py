from .base import Formula


class Flac(Formula):
    url = 'https://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz'
    depends_on = [
        'libogg',
    ]

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-dependency-tracking',
            '--disable-debug',
            '--enable-static',
            '--disable-asm-optimizations',  # for 32 bit
        ]
