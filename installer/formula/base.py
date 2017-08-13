import os
from installer.builders import Make
from utils import downloader, archiver


class Formula(object):
    url = None
    depends_on = None  # TODO: install dependencies automatically
    builder_classes = [
        Make,
    ]

    def __init__(self, prefix, download_to, extract_to, env=None, src=None):
        self.prefix = prefix
        self.download_to = download_to
        self.extract_to = extract_to
        self.env = env
        self.src = src

    @property
    def options(self):
        return []

    def execute(self):
        self.download()
        self.setup_env()
        self.install()

    def download(self):
        if self.src is None:
            archive_path = downloader.download(self.url, self.download_to)
            self.src = archiver.extract(archive_path, self.extract_to)
        return self.src

    def setup_env(self):
        pass

    def install(self):
        if not os.path.exists(self.prefix):
            os.mkdir(self.prefix)

        for builder_class in self.builder_classes:
            builder_class(self.src, self.options, self.env.setup()).run()
