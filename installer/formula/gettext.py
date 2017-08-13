from .base import Formula


class Gettext(Formula):
    url = 'https://ftp.gnu.org/gnu/gettext/gettext-0.19.8.1.tar.xz'

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-dependency-tracking',
            '--disable-silent-rules',
            '--disable-debug',
            '--with-included-gettext',
            '--with-included-glib',
            '--with-included-libcroco',
            '--with-included-libunistring',
            '--with-emacs',
            # '--with-lispdir=#{elisp}',
            '--disable-java',
            '--disable-csharp',
            # Don't use VCS systems to create these archives
            '--without-git',
            '--without-cvs',
            '--without-xz'
        ]
