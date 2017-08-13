import os
import logging
import tarfile

logger = logging.getLogger(__name__)


class ArchiverException(Exception):
    pass


class dirs_diff(object):
    def __init__(self, path):
        self.path = path
        self.before = []
        self.after = []

    def __enter__(self):
        if os.path.exists(self.path):
            self.before = os.listdir(self.path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.after = list(set(os.listdir(self.path)).difference(self.before))


def extract(src_file, dst_dir):

    with dirs_diff(dst_dir) as diff:
        with tarfile.open(src_file) as archive:
            archive.extractall(dst_dir)

    if not diff.after:
        msg = f'Failed to locate extracted content {src_file} at {dst_dir}.'
        raise ArchiverException(msg)

    return os.path.join(dst_dir, diff.after[0])
