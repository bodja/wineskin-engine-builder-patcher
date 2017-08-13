from installer.builders import Make as BaseMake
from .base import Formula


class Make(BaseMake):
    def configure(self):
        return self.shell.run('./Configure', *self.opts)


class Openssl(Formula):
    url = 'https://www.openssl.org/source/openssl-1.0.2l.tar.gz'
    builder_classes = (
        Make,
    )

    arch_32 = ['darwin-i386-cc']
    arch_64 = ['darwin64-x86_64-cc', 'enable-ec_nistp_64_gcc_128']

    def get_arch_flags(self):
        if self.env.universal_bin:
            return self.arch_32  # TODO make proper build e.g. https://gist.github.com/Sanjo/2722478#file-build_openssl_a-sh
        return self.arch_64

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            f'--openssldir={self.prefix}',
            'no-ssl2',
            'zlib-dynamic',
            'shared',
            'enable-cms',
        ] + self.get_arch_flags()
