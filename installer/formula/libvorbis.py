from .base import Formula


class Libvorbis(Formula):
    url = 'https://downloads.xiph.org/releases/vorbis/libvorbis-1.3.5.tar.xz'
    depends_on = [
        'libogg',
    ]

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-dependency-tracking',
        ]
