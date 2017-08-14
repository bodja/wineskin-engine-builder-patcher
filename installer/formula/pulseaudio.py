import config
from .base import Formula


class Pulseaudio(Formula):
    url = 'https://www.freedesktop.org/software/pulseaudio/releases/pulseaudio-10.99.1.tar.xz'  # noqa

    depends_on = [
        'libtool',
        'json-c',
        'libsndfile',
        'libsoxr',
        'openssl',
    ]

    def get_arch_flags(self):
        if self.env.universal_bin:
            return [
                '--enable-mac-universal',
            ]
        return []

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            f'--with-libintl-prefix={self.prefix}',
            '--disable-dependency-tracking',
            '--disable-silent-rules',
            '--enable-coreaudio-output',
            '--disable-neon-opt',
            f'--with-mac-sysroot={config.SDK_PATH}',
            f'--with-mac-version-min={config.MIN_SDK_VERSION}',
            '--disable-x11',
        ] + self.get_arch_flags()
