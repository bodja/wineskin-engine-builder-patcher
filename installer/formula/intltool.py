from .base import Formula


class Intltool(Formula):
    url = 'https://launchpad.net/intltool/trunk/0.51.0/+download/intltool-0.51.0.tar.gz'  # noqa

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
        ]
