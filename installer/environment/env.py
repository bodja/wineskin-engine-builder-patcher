import os

from .properties import ListOption, CFlagArchListOption, EnvProperty


class Env(object):
    # simple attrs
    arch_32 = ['-arch i386', '-m32']
    arch_64 = ['-arch x86_64', '-m64']
    arch_universal = arch_32 + arch_64

    prefix = '/tmp/Wineskin'
    bins = f'{prefix}/bin'
    libs = f'{prefix}/lib'
    includes = f'{prefix}/include'

    # environment attrs
    PKG_CONFIG_PATH = EnvProperty(f'{libs}/pkgconfig')
    CPPFLAGS = ListOption([f'-I{includes}'])
    CFLAGS = CFlagArchListOption([f'-I{includes}'])
    CXXFLAGS = CFlagArchListOption([f'-I{includes}'])
    LDFLAGS = CFlagArchListOption([f'-L{libs}'])

    def __init__(self, universal_bin=False):
        self.universal_bin = universal_bin

    def setup(self):
        os_env = os.environ.copy()
        os_env['PATH'] = f"{self.bins}:{os_env['PATH']}"
        os_env['CPPFLAGS'] = self.CPPFLAGS
        os_env['CFLAGS'] = self.CFLAGS
        os_env['CXXFLAGS'] = self.CXXFLAGS
        os_env['LDFLAGS'] = self.LDFLAGS
        os_env['PKG_CONFIG_PATH'] = self.PKG_CONFIG_PATH
        os_env['PKG_CONFIG_LIBDIR'] = self.PKG_CONFIG_PATH
        return os_env
