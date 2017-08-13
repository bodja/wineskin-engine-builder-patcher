from .base import Formula


class JsonC(Formula):
    url = 'https://github.com/json-c/json-c/archive/json-c-0.12-20140410.tar.gz'  # noqa

    @property
    def options(self):
        return [
            f'--prefix={self.prefix}',
            '--disable-silent-rules',
            '--disable-dependency-tracking',
        ]
