from installer.builders import CMake
from .base import Formula


class Libsoxr(Formula):
    url = 'https://downloads.sourceforge.net/project/soxr/soxr-0.1.2-Source.tar.xz'  # noqa

    builder_classes = [CMake]

    @property
    def options(self):
        return [
            f'-DCMAKE_INSTALL_PREFIX={self.prefix}',
        ]
