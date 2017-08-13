from .base import Formula


class Freetype(Formula):
    url = 'https://downloads.sourceforge.net/project/freetype/freetype2/2.8/freetype-2.8.tar.bz2'  # noqa

    depends_on = [
        'libpng'
    ]

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--without-harfbuzz',
        ]
