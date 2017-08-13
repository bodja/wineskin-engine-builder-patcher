from installer.builders import Make, Autoreconf
from .base import Formula


class Libsndfile(Formula):
    url = 'http://www.mega-nerd.com/libsndfile/files/libsndfile-1.0.28.tar.gz'
    builder_classes = (
        Autoreconf,
        Make
    )

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-dependency-tracking',
        ]

    depends_on = [
        'flac',
        'libogg',
        'libvorbis',
    ]
