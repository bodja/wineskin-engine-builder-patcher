from .base import Formula


class Pulseaudio(Formula):
    url = 'https://www.freedesktop.org/software/pulseaudio/releases' \
          '/pulseaudio-10.99.1.tar.xz'  # noqa

    depends_on = [
        'libtool',  # +
        'json-c',  # +
        'libsndfile',  # +
        'libsoxr',  # -
        'openssl',  # -
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
            '--with-mac-sysroot=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk',
            '--with-mac-version-min=10.11',
            '--disable-x11',
        ] + self.get_arch_flags()
